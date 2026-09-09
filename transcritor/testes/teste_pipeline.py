# -*- coding: utf-8 -*-
"""
Teste da logica que nao depende de internet.

Substitui as duas etapas de rede (baixar o audio e rodar o Whisper) por
dublês, e verifica o resto de ponta a ponta: nome do arquivo, conteudo,
deteccao de repetido, arquivo unico acumulado e remocao do audio.

Rodar:  python testes/teste_pipeline.py
"""

import shutil
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import transcrever as t  # noqa: E402

FALHAS = []
PASTAS_DE_AUDIO = []


def checar(condicao, descricao):
    print(f"  {'ok  ' if condicao else 'FALHOU'}  {descricao}")
    if not condicao:
        FALHAS.append(descricao)


def instalar_dubles():
    def meta_falsa(url, cfg):
        return {
            "id": "DdD-pemRZb8",
            "titulo": "Reel de teste",
            "autor": "Joao da Silva",
            "duracao": 95,
            "plataforma": t.detectar_plataforma(url),
            "url": url,
        }

    def download_falso(url, cfg, destino):
        caminho = destino / "audio.m4a"
        caminho.write_bytes(b"audio falso")
        PASTAS_DE_AUDIO.append(destino)
        return caminho

    def whisper_falso(caminho_audio, cfg):
        assert Path(caminho_audio).exists(), "o audio sumiu antes da transcricao"
        return {
            "idioma": "pt",
            "confianca": 0.987,
            "segmentos": [
                {"inicio": 0.0, "fim": 3.2, "texto": "Bom dia, pessoal."},
                {"inicio": 3.2, "fim": 8.9, "texto": "Hoje eu vou falar de tres coisas."},
                {"inicio": 65.0, "fim": 70.4, "texto": "E era isso, ate a proxima."},
            ],
        }

    t.ler_metadados = meta_falsa
    t.baixar_audio = download_falso
    t.transcrever = whisper_falso


def main():
    instalar_dubles()
    pasta = Path(tempfile.mkdtemp(prefix="teste_saida_"))
    cfg = dict(t.CONFIG_PADRAO, pasta_saida=str(pasta), modelo="medium")
    url = "https://www.instagram.com/reel/DdD-pemRZb8/?stkn=abc"

    print("\n1) Leitura de varios links colados de qualquer jeito")
    colado = (
        "olha esses: https://www.instagram.com/reel/AAA/ e tambem\n"
        "https://www.tiktok.com/@x/video/123, mais https://youtu.be/BBB.\n"
        "e o repetido https://www.instagram.com/reel/AAA/"
    )
    links = t.extrair_links(colado)
    checar(len(links) == 3, f"achou 3 links unicos (achou {len(links)})")
    checar(
        links[1] == "https://www.tiktok.com/@x/video/123",
        "tirou a virgula grudada no fim do link",
    )
    checar(links[2] == "https://youtu.be/BBB", "tirou o ponto final grudado")

    print("\n2) Primeira transcricao")
    r1 = t.rodar([url], cfg, log=lambda *_: None)[0]
    checar(r1["status"] == "ok", "transcreveu")
    arquivo = Path(r1["arquivo"])
    checar(arquivo.exists(), "criou o arquivo de texto")
    checar(
        arquivo.name.endswith("_instagram_joao-da-silva_DdD-pemRZb8.txt"),
        # o ID tem de sair com as maiusculas originais
        f"nome do arquivo no formato combinado ({arquivo.name})",
    )

    texto = arquivo.read_text(encoding="utf-8")
    for campo in ["Autor:", "Plataforma:", "Link:", "Duracao:", "Idioma:"]:
        checar(campo in texto, f"tem o campo {campo}")
    checar("1:35" in texto, "duracao formatada como 1:35")
    checar("portugues" in texto, "idioma em portugues por extenso")
    checar("99%" in texto, "mostra a confianca da deteccao (0,987 -> 99%)")
    checar("TRANSCRICAO CORRIDA" in texto, "tem a versao corrida")
    checar("COM MARCACAO DE TEMPO" in texto, "tem a versao com tempo")
    checar(
        "Bom dia, pessoal. Hoje eu vou falar de tres coisas." in texto,
        "versao corrida junta as falas numa linha so",
    )
    checar("[00:01:05] E era isso" in texto, "carimbo de tempo correto")

    print("\n3) Arquivo unico que acumula")
    mestre = pasta / cfg["arquivo_mestre"]
    checar(mestre.exists(), "criou o arquivo unico")
    conteudo_mestre = mestre.read_text(encoding="utf-8")
    checar(url in conteudo_mestre, "a entrada tem o link")
    checar(arquivo.name in conteudo_mestre, "a entrada aponta pro arquivo completo")

    print("\n4) O audio nao ficou guardado")
    checar(
        all(not p.exists() for p in PASTAS_DE_AUDIO),
        "a pasta temporaria de audio foi apagada",
    )

    print("\n5) Mesmo video de novo: avisa e nao sobrescreve")
    marca = arquivo.stat().st_mtime_ns
    tamanho_mestre = mestre.stat().st_size
    avisos = []
    r2 = t.rodar([url], cfg, log=avisos.append)[0]
    checar(r2["status"] == "pulado", "detectou que ja tinha sido transcrito")
    checar(
        any("JA TRANSCRITO" in linha for linha in avisos), "avisou na tela"
    )
    checar(arquivo.stat().st_mtime_ns == marca, "nao mexeu no arquivo existente")
    checar(
        mestre.stat().st_size == tamanho_mestre,
        "nao duplicou a entrada no arquivo unico",
    )

    print("\n6) Um link que da erro nao derruba os outros")
    def as_vezes_falha(u, cfg_):
        if "quebrado" in u:
            raise RuntimeError("video privado")
        return {
            "id": "OUTRO", "titulo": "Outro", "autor": "Maria",
            "duracao": 30, "plataforma": "youtube", "url": u,
        }

    t.ler_metadados = as_vezes_falha
    res = t.rodar(
        ["https://youtu.be/quebrado", "https://youtu.be/bom"],
        cfg, log=lambda *_: None,
    )
    checar(res[0]["status"] == "erro", "marcou o link problematico como erro")
    checar(res[1]["status"] == "ok", "seguiu e transcreveu o link seguinte")

    shutil.rmtree(pasta, ignore_errors=True)

    print("\n" + "=" * 55)
    if FALHAS:
        print(f"{len(FALHAS)} FALHA(S):")
        for f in FALHAS:
            print(f"  - {f}")
        return 1
    print("Todos os testes passaram.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

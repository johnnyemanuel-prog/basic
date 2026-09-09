#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Transcritor de video por link - Instagram, TikTok e YouTube.

Baixa somente o audio, transcreve localmente (Whisper via faster-whisper),
detecta o idioma sozinho e salva um arquivo de texto por video.
Nada de audio sai da maquina; nao usa servico pago.
"""

import argparse
import datetime as dt
import json
import os
import re
import shutil
import sys
import tempfile
import unicodedata
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
CONFIG_PATH = APP_DIR / "config.json"

CONFIG_PADRAO = {
    # Pasta onde as transcricoes sao salvas. Aponte para a sua pasta do
    # Google Drive sincronizada se quiser que subam sozinhas.
    "pasta_saida": "",
    # small = rapido / medium = equilibrado / large-v3 = melhor qualidade
    "modelo": "medium",
    # Navegador de onde puxar cookies quando o site exigir login.
    # "" = desligado. Ex.: "chrome", "edge", "firefox", "brave".
    "cookies_navegador": "",
    # Arquivo unico que acumula todas as transcricoes.
    "arquivo_mestre": "TODAS_AS_TRANSCRICOES.md",
    # Dica de idioma. "" = detectar sozinho (recomendado).
    "idioma_fixo": "",
}


# --------------------------------------------------------------------------
# configuracao
# --------------------------------------------------------------------------

def carregar_config():
    cfg = dict(CONFIG_PADRAO)
    if CONFIG_PATH.exists():
        try:
            cfg.update(json.loads(CONFIG_PATH.read_text(encoding="utf-8")))
        except (json.JSONDecodeError, OSError) as e:
            print(f"[aviso] config.json ilegivel ({e}); usando padroes.")
    if not cfg["pasta_saida"]:
        cfg["pasta_saida"] = str(Path.home() / "Transcricoes")
    return cfg


def salvar_config(cfg):
    CONFIG_PATH.write_text(
        json.dumps(cfg, indent=2, ensure_ascii=False), encoding="utf-8"
    )


# --------------------------------------------------------------------------
# utilidades
# --------------------------------------------------------------------------

PLATAFORMAS = {
    "instagram": "instagram",
    "tiktok": "tiktok",
    "youtube": "youtube",
    "youtu.be": "youtube",
}


def detectar_plataforma(url, extractor=""):
    alvo = f"{url} {extractor}".lower()
    for chave, nome in PLATAFORMAS.items():
        if chave in alvo:
            return nome
    return (extractor or "desconhecida").lower()


def limpar_nome(texto, limite=40, minusculas=True, reserva="sem-autor"):
    """Reduz um texto a algo seguro para nome de arquivo no Windows.

    minusculas=False preserva maiusculas/minusculas: os identificadores de
    video do Instagram e do YouTube diferenciam as duas (DdD-pemRZb8), e
    baixar por eles em minusculas nao funciona.
    """
    texto = unicodedata.normalize("NFKD", str(texto or ""))
    texto = texto.encode("ascii", "ignore").decode("ascii")
    texto = re.sub(r"[^A-Za-z0-9]+", "-", texto).strip("-")
    if minusculas:
        texto = texto.lower()
    return texto[:limite] or reserva


def formatar_duracao(segundos):
    if not segundos:
        return "desconhecida"
    segundos = int(segundos)
    h, resto = divmod(segundos, 3600)
    m, s = divmod(resto, 60)
    return f"{h:d}:{m:02d}:{s:02d}" if h else f"{m:d}:{s:02d}"


def carimbo(segundos):
    segundos = max(0, int(segundos))
    h, resto = divmod(segundos, 3600)
    m, s = divmod(resto, 60)
    return f"[{h:02d}:{m:02d}:{s:02d}]"


NOMES_IDIOMA = {
    "pt": "portugues", "en": "ingles", "es": "espanhol", "fr": "frances",
    "it": "italiano", "de": "alemao", "ja": "japones", "ko": "coreano",
    "zh": "chines", "ru": "russo", "ar": "arabe", "nl": "holandes",
}


def nome_idioma(codigo):
    return NOMES_IDIOMA.get(codigo, codigo or "desconhecido")


# --------------------------------------------------------------------------
# indice (para nao transcrever duas vezes)
# --------------------------------------------------------------------------

def caminho_indice(pasta_saida):
    return Path(pasta_saida) / "_indice.json"


def carregar_indice(pasta_saida):
    caminho = caminho_indice(pasta_saida)
    if caminho.exists():
        try:
            return json.loads(caminho.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            print("[aviso] _indice.json corrompido; comecando um novo.")
    return {}


def salvar_indice(pasta_saida, indice):
    caminho_indice(pasta_saida).write_text(
        json.dumps(indice, indent=2, ensure_ascii=False), encoding="utf-8"
    )


# --------------------------------------------------------------------------
# etapas
# --------------------------------------------------------------------------

def opcoes_ytdlp(cfg, extras=None):
    opts = {
        "quiet": True,
        "no_warnings": True,
        "noprogress": True,
        # so audio, nunca o video inteiro
        "format": "bestaudio/best",
        "noplaylist": True,
    }
    if cfg.get("cookies_navegador"):
        opts["cookiesfrombrowser"] = (cfg["cookies_navegador"],)
    if extras:
        opts.update(extras)
    return opts


def ler_metadados(url, cfg):
    """Le titulo/autor/duracao sem baixar nada."""
    from yt_dlp import YoutubeDL

    with YoutubeDL(opcoes_ytdlp(cfg)) as ydl:
        info = ydl.extract_info(url, download=False)
    if info.get("entries"):
        info = info["entries"][0]

    autor = (
        info.get("uploader")
        or info.get("channel")
        or info.get("uploader_id")
        or "desconhecido"
    )
    return {
        "id": info.get("id") or "sem-id",
        "titulo": info.get("title") or "sem titulo",
        "autor": autor,
        "duracao": info.get("duration"),
        "plataforma": detectar_plataforma(url, info.get("extractor_key", "")),
        "url": info.get("webpage_url") or url,
    }


def baixar_audio(url, cfg, destino):
    """Baixa apenas a faixa de audio. Devolve o caminho do arquivo."""
    from yt_dlp import YoutubeDL

    modelo_nome = str(destino / "audio.%(ext)s")
    with YoutubeDL(opcoes_ytdlp(cfg, {"outtmpl": modelo_nome})) as ydl:
        ydl.extract_info(url, download=True)

    arquivos = [p for p in destino.iterdir() if p.is_file()]
    if not arquivos:
        raise RuntimeError("o download nao produziu nenhum arquivo de audio")
    return max(arquivos, key=lambda p: p.stat().st_size)


_MODELO_CACHE = {}


def carregar_modelo(nome_modelo):
    """Carrega o Whisper uma vez por execucao; usa a placa NVIDIA se houver."""
    if nome_modelo in _MODELO_CACHE:
        return _MODELO_CACHE[nome_modelo]

    from faster_whisper import WhisperModel

    tentativas = [("cuda", "float16"), ("cpu", "int8")]
    ultimo_erro = None
    for dispositivo, precisao in tentativas:
        try:
            modelo = WhisperModel(
                nome_modelo, device=dispositivo, compute_type=precisao
            )
            print(f"[modelo] {nome_modelo} em {dispositivo} ({precisao})")
            _MODELO_CACHE[nome_modelo] = modelo
            return modelo
        except Exception as e:  # placa ausente, driver velho, sem VRAM
            ultimo_erro = e
    raise RuntimeError(f"nao foi possivel carregar o modelo: {ultimo_erro}")


def transcrever(caminho_audio, cfg):
    modelo = carregar_modelo(cfg["modelo"])
    segmentos, info = modelo.transcribe(
        str(caminho_audio),
        language=cfg.get("idioma_fixo") or None,
        vad_filter=True,
        beam_size=5,
    )
    segmentos = list(segmentos)
    return {
        "idioma": info.language,
        "confianca": info.language_probability,
        "segmentos": [
            {"inicio": s.start, "fim": s.end, "texto": s.text.strip()}
            for s in segmentos
        ],
    }


# --------------------------------------------------------------------------
# escrita
# --------------------------------------------------------------------------

def montar_texto(meta, resultado, data_iso):
    corrida = " ".join(s["texto"] for s in resultado["segmentos"]).strip()
    marcado = "\n".join(
        f"{carimbo(s['inicio'])} {s['texto']}" for s in resultado["segmentos"]
    )
    idioma = nome_idioma(resultado["idioma"])
    confianca = f"{resultado['confianca'] * 100:.0f}%"

    return (
        f"Titulo:     {meta['titulo']}\n"
        f"Autor:      {meta['autor']}\n"
        f"Plataforma: {meta['plataforma']}\n"
        f"Link:       {meta['url']}\n"
        f"Duracao:    {formatar_duracao(meta['duracao'])}\n"
        f"Idioma:     {idioma} (deteccao automatica, confianca {confianca})\n"
        f"Transcrito: {data_iso}\n"
        f"\n{'=' * 70}\nTRANSCRICAO CORRIDA\n{'=' * 70}\n\n"
        f"{corrida or '(nenhuma fala detectada)'}\n"
        f"\n{'=' * 70}\nCOM MARCACAO DE TEMPO\n{'=' * 70}\n\n"
        f"{marcado or '(nenhuma fala detectada)'}\n"
    ), corrida, idioma, confianca


def anexar_ao_mestre(cfg, meta, corrida, idioma, data_iso, nome_arquivo):
    mestre = Path(cfg["pasta_saida"]) / cfg["arquivo_mestre"]
    novo = not mestre.exists()
    with mestre.open("a", encoding="utf-8") as f:
        if novo:
            f.write("# Todas as transcricoes\n")
        f.write(
            f"\n\n---\n\n## {data_iso} - {meta['titulo']}\n\n"
            f"- Autor: {meta['autor']}\n"
            f"- Plataforma: {meta['plataforma']}\n"
            f"- Link: {meta['url']}\n"
            f"- Duracao: {formatar_duracao(meta['duracao'])}\n"
            f"- Idioma: {idioma}\n"
            f"- Arquivo completo (com marcacao de tempo): `{nome_arquivo}`\n\n"
            f"{corrida or '(nenhuma fala detectada)'}\n"
        )
    return mestre


# --------------------------------------------------------------------------
# fluxo por link
# --------------------------------------------------------------------------

def processar(url, cfg, indice, log=print):
    log(f"\n>> {url}")
    log("   lendo dados do video...")
    meta = ler_metadados(url, cfg)
    chave = f"{meta['plataforma']}:{meta['id']}"

    if chave in indice:
        anterior = indice[chave]
        log(f"   JA TRANSCRITO em {anterior['data']} -> {anterior['arquivo']}")
        log("   pulando (nada foi sobrescrito).")
        return {"status": "pulado", "meta": meta, "anterior": anterior}

    log(f"   autor: {meta['autor']} | duracao: {formatar_duracao(meta['duracao'])}")

    temporaria = Path(tempfile.mkdtemp(prefix="transcritor_"))
    try:
        log("   baixando so o audio...")
        audio = baixar_audio(url, cfg, temporaria)
        log(f"   transcrevendo localmente (modelo {cfg['modelo']})...")
        resultado = transcrever(audio, cfg)
    finally:
        # o audio nunca fica guardado
        shutil.rmtree(temporaria, ignore_errors=True)

    data_iso = dt.date.today().isoformat()
    texto, corrida, idioma, confianca = montar_texto(meta, resultado, data_iso)
    log(f"   idioma detectado: {idioma} (confianca {confianca})")

    nome_arquivo = (
        f"{data_iso}_{meta['plataforma']}_"
        f"{limpar_nome(meta['autor'])}_"
        f"{limpar_nome(meta['id'], 30, minusculas=False, reserva='sem-id')}.txt"
    )
    destino = Path(cfg["pasta_saida"]) / nome_arquivo
    destino.write_text(texto, encoding="utf-8")

    mestre = anexar_ao_mestre(cfg, meta, corrida, idioma, data_iso, nome_arquivo)

    indice[chave] = {
        "data": data_iso,
        "arquivo": nome_arquivo,
        "titulo": meta["titulo"],
        "autor": meta["autor"],
        "url": meta["url"],
        "idioma": idioma,
    }
    salvar_indice(cfg["pasta_saida"], indice)

    log(f"   salvo: {destino}")
    log(f"   somado ao arquivo unico: {mestre.name}")
    return {
        "status": "ok",
        "meta": meta,
        "arquivo": destino,
        "idioma": idioma,
        "corrida": corrida,
    }


def extrair_links(texto):
    """Pega todos os links de um texto colado de qualquer jeito."""
    achados = re.findall(r"https?://[^\s<>\"')]+", texto or "")
    unicos = []
    for link in achados:
        link = link.rstrip(".,;")
        if link not in unicos:
            unicos.append(link)
    return unicos


def rodar(urls, cfg, log=print):
    Path(cfg["pasta_saida"]).mkdir(parents=True, exist_ok=True)
    indice = carregar_indice(cfg["pasta_saida"])
    resultados = []
    for url in urls:
        try:
            resultados.append(processar(url, cfg, indice, log=log))
        except Exception as e:
            log(f"   ERRO: {e}")
            resultados.append({"status": "erro", "url": url, "erro": str(e)})

    ok = sum(1 for r in resultados if r["status"] == "ok")
    pulados = sum(1 for r in resultados if r["status"] == "pulado")
    erros = sum(1 for r in resultados if r["status"] == "erro")
    log(f"\nResumo: {ok} transcrito(s), {pulados} pulado(s), {erros} com erro.")
    log(f"Pasta: {cfg['pasta_saida']}")
    return resultados


# --------------------------------------------------------------------------
# entrada
# --------------------------------------------------------------------------

def modo_colar(cfg):
    """Modo texto: cole os links e de Enter duas vezes.

    Serve de reserva para o Python portatil, que vem sem a biblioteca
    grafica (tkinter) e portanto nao consegue abrir a janelinha.
    """
    print("=" * 60)
    print("TRANSCRITOR DE VIDEO")
    print("=" * 60)
    print(f"Pasta de saida: {cfg['pasta_saida']}")
    print(f"Qualidade: {cfg['modelo']}")
    print("\nCole os links (Instagram, TikTok ou YouTube).")
    print("Quando terminar, de Enter numa linha vazia.\n")

    linhas = []
    while True:
        try:
            linha = input("> ")
        except EOFError:
            break
        if not linha.strip():
            break
        linhas.append(linha)

    links = extrair_links("\n".join(linhas))
    if not links:
        print("\nNenhum link encontrado.")
        input("Enter para fechar.")
        return 1

    print(f"\n{len(links)} link(s) para processar.\n")
    resultados = rodar(links, cfg)
    input("\nEnter para fechar.")
    return 0 if all(r["status"] != "erro" for r in resultados) else 1


def abrir_interface(cfg):
    """Tenta a janelinha; se nao houver tkinter, usa o modo texto."""
    try:
        from janela import abrir_janela
    except ImportError:
        print("[aviso] este Python nao tem a biblioteca grafica; "
              "usando o modo de colar pelo teclado.\n")
        return modo_colar(cfg)
    abrir_janela(cfg)
    return 0


def main():
    p = argparse.ArgumentParser(
        description="Transcreve videos do Instagram, TikTok e YouTube por link."
    )
    p.add_argument("links", nargs="*", help="um ou mais links")
    p.add_argument("--pasta", help="pasta de saida (sobrepoe o config.json)")
    p.add_argument("--modelo", help="small, medium ou large-v3")
    p.add_argument("--cookies", help="navegador para cookies: chrome, edge, firefox")
    p.add_argument("--janela", action="store_true", help="abre a janelinha")
    args = p.parse_args()

    cfg = carregar_config()
    if args.pasta:
        cfg["pasta_saida"] = args.pasta
    if args.modelo:
        cfg["modelo"] = args.modelo
    if args.cookies is not None:
        cfg["cookies_navegador"] = args.cookies

    if args.janela or (not args.links and sys.stdin.isatty()):
        return abrir_interface(cfg)

    links = args.links or extrair_links(sys.stdin.read())
    if not links:
        print("Nenhum link encontrado. Cole os links como argumento.")
        return 1

    print(f"{len(links)} link(s) para processar.")
    resultados = rodar(links, cfg)
    return 0 if all(r["status"] != "erro" for r in resultados) else 1


if __name__ == "__main__":
    sys.exit(main())

# Transcritor de vídeo por link

Cola um link (ou vários) do Instagram, TikTok ou YouTube e recebe a transcrição
em texto. O áudio é baixado, transcrito **dentro do seu computador** e apagado
em seguida. Nada é enviado para fora, não há custo por minuto.

---

## Instalar (só na primeira vez)

Baixe esta pasta para o computador e dê **dois cliques** em um destes arquivos:

| Situação | Arquivo |
|---|---|
| Computador de casa (tem Python, você é administrador) | `INSTALAR_casa.bat` |
| Qualquer outro computador (sem Python, sem administrador) | `INSTALAR_sem_admin.bat` |

O segundo não instala nada no Windows — baixa um Python portátil que fica
dentro desta própria pasta. Pode rodar em computador de trabalho sem permissão.

Na primeira transcrição, o programa ainda baixa o modelo de reconhecimento de
fala (cerca de 1,5 GB para o `medium`). Isso acontece **uma vez só**.

## Usar no dia a dia

Dois cliques em **`Transcritor.bat`**. Abre uma janela: cole os links, um por
linha, e clique em *Transcrever*. Na máquina sem administrador, em vez da
janela abre uma tela preta onde você cola os links e dá Enter duas vezes.

## O que você recebe

**Um arquivo `.txt` por vídeo**, com nome no formato
`2026-09-09_instagram_nomedoautor_DdD-pemRZb8.txt`, contendo:

- título, autor, plataforma, link, duração
- o idioma que foi detectado automaticamente, e o quanto o programa está seguro disso
- a transcrição corrida (texto contínuo, para ler ou copiar)
- a transcrição com marcação de tempo (`[00:01:05] ...`, para achar o trecho no vídeo)

**Mais um arquivo único que acumula tudo**: `TODAS_AS_TRANSCRICOES.md`. Cada
vídeo novo vira uma entrada nova no fim, com a data, o link e o texto corrido.
Esse é o arquivo para deixar no Google Drive.

## Mandar para o Google Drive automaticamente

Não precisa de senha nem configuração de nuvem. Instale o Google Drive para
computador, e aponte a pasta de saída para dentro dele: na janela, clique em
*Pasta de saída...* e escolha algo como `G:\Meu Drive\Transcrições`. O Drive
sincroniza sozinho a partir daí.

## Vídeo repetido

Se você colar um link que já foi transcrito antes, o programa avisa na tela,
diz a data e o arquivo de antes, e **pula sem sobrescrever nada**. O controle
fica no arquivo `_indice.json`, dentro da pasta de saída.

## Quando o Instagram pedir login

Reels às vezes só abrem para quem está logado. Se der erro de login, abra o
`config.json` no Bloco de Notas e mude a linha dos cookies para o navegador
onde você usa o Instagram:

```json
"cookies_navegador": "chrome"
```

Vale `chrome`, `edge`, `firefox`, `brave` ou `opera`. O programa passa a usar a
sessão já aberta nesse navegador. Feche o navegador antes de rodar.

## Ajustes no `config.json`

| Item | Para que serve |
|---|---|
| `pasta_saida` | Onde salvar. Vazio = pasta `Transcricoes` na sua pasta de usuário. |
| `modelo` | `small` (rápido), `medium` (equilibrado, padrão), `large-v3` (melhor). |
| `cookies_navegador` | Navegador de onde puxar o login. Vazio = desligado. |
| `arquivo_mestre` | Nome do arquivo que acumula tudo. |
| `idioma_fixo` | Vazio = detectar sozinho. `pt` força português. |

Na máquina de casa, com a RTX 3050, o `medium` roda na placa de vídeo e fica
bem rápido. Na máquina de 8 GB sem placa, o instalador já deixa no `small`.

## Se der problema

Rode a verificação interna, que testa a lógica sem precisar de internet:

```
python testes/teste_pipeline.py
```

Se acusar falha, ou se der erro na hora de usar, copie a mensagem inteira e
mande para o Claude.

## Para quem quiser usar por linha de comando

```
python transcrever.py "https://youtu.be/AAA" "https://www.tiktok.com/@x/video/1"
python transcrever.py --modelo large-v3 --pasta "D:\Textos" "https://..."
python transcrever.py --cookies chrome "https://www.instagram.com/reel/..."
```

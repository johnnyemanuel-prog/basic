"""Monta a trilha de áudio do Lumínia Ep1 (174 s) a partir dos arquivos em raw/.

Cada item: (arquivo, início na timeline em s, filtros extras aplicados ao clipe).
Os filtros extras rodam antes do atraso, então tempos de fade são relativos ao clipe.
"""
import os
import subprocess
import sys

import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
TOTAL = 174.0

# Recortes das amostras de voz do Enzo e do Dario (limite de 3 vozes salvas na conta).
ENZO_1 = "atrim=0.08:2.55,asetpts=PTS-STARTPTS"   # "Aproxima o pulso aí, tio."
ENZO_2 = "atrim=2.70:4.15,asetpts=PTS-STARTPTS"   # "Não dá... o senhor não tá na rede."
ENZO_3 = "atrim=4.60:9.87,asetpts=PTS-STARTPTS"   # "Desculpa. Eu tenho que ir. ..."
DARIO = "atrim=0:1.45,asetpts=PTS-STARTPTS"       # "Meu casal favorito!"

TRACKS = [
    # --- Cena 1: avenida, música de espetáculo + multidão em decrescendo até 0:12
    ("mus_festiva.mp3", 0.0, "atrim=0:12,volume=0.55,afade=t=out:st=2:d=10"),
    ("amb_multidao.mp3", 0.0, "atrim=0:12,volume=0.7,afade=t=out:st=3:d=9"),
    # --- Cena 2+3: delegacia / mendigo
    ("amb_drone.mp3", 12.0, "aloop=loop=-1:size=2147483647,atrim=0:60,volume=0.35,afade=t=in:d=1,afade=t=out:st=58.5:d=1.5"),
    ("v_mendigo1.mp3", 18.2, "volume=1.0"),
    ("enzo_preview.mp3", 34.2, ENZO_1),
    ("sfx_beeps.mp3", 40.0, "volume=0.5,afade=t=out:st=9.5:d=1.5"),
    ("enzo_preview.mp3", 51.2, ENZO_2),
    ("v_mendigo2.mp3", 57.2, "volume=1.0"),
    ("sfx_drone_perto.mp3", 62.0, "volume=0.6"),
    ("enzo_preview.mp3", 64.2, ENZO_3),
    # --- Cena 4: música pop dos fones domina; pensamento abafado por baixo
    ("mus_pop.mp3", 72.0, "atrim=0:12,volume=0.9,afade=t=in:d=0.3,afade=t=out:st=7:d=5"),
    ("v_enzo_pensamento.mp3", 72.8, "lowpass=f=900,highpass=f=150,aecho=0.8:0.6:40:0.3,volume=0.55"),
    # --- Cena 5: closet, ventilação de leito até a virada pro carro (1:58)
    ("amb_ventilacao.mp3", 82.0, "aloop=loop=-1:size=2147483647,atrim=0:36,volume=0.3,afade=t=in:d=1.5,afade=t=out:st=35:d=1"),
    ("v_ari1.mp3", 84.2, "volume=1.0"),
    # --- Cena 6: Larissa
    ("v_larissa1.mp3", 98.2, "volume=1.0"),
    ("v_ari2.mp3", 110.2, "volume=1.0"),
    # --- Cena 7: carro blindado
    ("amb_carro.mp3", 118.0, "aloop=loop=-1:size=2147483647,atrim=0:36,volume=0.4,afade=t=in:d=1,afade=t=out:st=35:d=1"),
    ("v_ari3.mp3", 120.2, "volume=1.0"),
    ("sfx_tap.mp3", 127.7, "volume=0.35"),
    ("v_larissa2.mp3", 128.2, "volume=1.0"),
    ("v_ari4.mp3", 132.2, "volume=1.0"),
    ("v_ari5.mp3", 148.2, "volume=1.0"),
    # --- Cena 8: chegada / cobertura — cliffhanger com corte seco em 2:54
    ("amb_chegada.mp3", 154.0, "volume=0.6"),
    ("mus_tensao.mp3", 154.0, "atrim=0:20,volume=0.5,afade=t=in:d=2"),
    ("sfx_whisky.mp3", 160.0, "volume=0.6"),
    ("dario_preview.mp3", 166.2, DARIO),
]


def build(out_wav):
    missing = [f for f, _, _ in TRACKS if not os.path.exists(os.path.join(RAW, f))]
    if missing:
        sys.exit(f"Arquivos faltando em raw/: {missing}")
    args = [FF, "-hide_banner", "-y"]
    for f, _, _ in TRACKS:
        args += ["-i", os.path.join(RAW, f)]
    chains, labels = [], []
    for i, (_, start, extra) in enumerate(TRACKS):
        ms = int(round(start * 1000))
        chains.append(
            f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,{extra},"
            f"adelay={ms}|{ms}[a{i}]"
        )
        labels.append(f"[a{i}]")
    chains.append(
        "".join(labels)
        + f"amix=inputs={len(labels)}:normalize=0:duration=longest,"
        f"alimiter=limit=0.9,atrim=0:{TOTAL},apad=whole_dur={TOTAL}[out]"
    )
    args += ["-filter_complex", ";".join(chains), "-map", "[out]",
             "-ar", "48000", "-c:a", "pcm_s16le", out_wav]
    subprocess.run(args, check=True)


if __name__ == "__main__":
    build(os.path.join(HERE, "Luminia_Ep1_trilha.wav"))

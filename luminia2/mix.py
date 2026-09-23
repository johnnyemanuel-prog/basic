"""Monta a trilha de áudio do Lumínia Ep2 (265 s, corte v06) a partir dos arquivos em raw/.

Cada item: (arquivo, início na timeline em s, filtros extras aplicados ao clipe).
Os inícios seguem os timecodes do script, que batem com os cards do vídeo v06.

Falas: d = Dario, a = Ari, L_ = Larissa, p = pensamento do Dario, v_narr = narrador.
"""
import os
import subprocess
import sys

import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
TOTAL = 265.0
LOOP = "aloop=loop=-1:size=2147483647"

# Pensamento: seco, próximo, sem projeção; realça graves e corta ar/ambiência.
THOUGHT = "highpass=f=90,lowpass=f=7000,equalizer=f=180:t=q:w=1:g=3,volume=0.9"

VOICES = [
    ("d01.wav", 0.30), ("d02.wav", 3.25),
    ("a01.wav", 12.30), ("a02.wav", 35.25),
    ("v_narr1.mp3", 44.30),
    ("L_a.wav", 63.30),
    ("d03.wav", 80.30), ("d04.wav", 88.30), ("d05.wav", 98.30), ("d06.wav", 108.25),
    ("d07.wav", 114.20), ("d08.wav", 117.00),
    ("a03.wav", 119.30), ("a04.wav", 126.30),
    ("d09.wav", 135.30),
    ("a05.wav", 140.35), ("L_b.wav", 149.20), ("a06.wav", 154.25), ("L_c.wav", 160.30),
    ("a07.wav", 165.25), ("d10.wav", 170.30), ("L_d.wav", 176.25), ("a08.wav", 182.25),
    ("d11.wav", 184.30), ("a09.wav", 189.30), ("d12.wav", 191.25), ("a10.wav", 193.00),
    ("L_e.wav", 195.25), ("a11.wav", 197.20), ("L_f.wav", 200.25),
    ("a12.wav", 214.30), ("d13.wav", 220.25),
    ("v_narr2.mp3", 237.30),
]
THOUGHTS = [("p01.wav", 228.30), ("p02.wav", 243.35), ("p03.wav", 254.30)]

# Música: quatro blocos com crossfade. Depois do CLIQUE (226) a cama cai ~7 dB.
MUSIC = [
    ("mus_1.mp3", 0.0, "atrim=0:66,volume=0.30,afade=t=in:d=0.05,afade=t=out:st=63:d=3"),
    ("mus_2.mp3", 63.0, "atrim=0:80,volume=0.30,afade=t=in:d=3,afade=t=out:st=76:d=4"),
    ("mus_3.wav", 139.0, "atrim=0:88,volume=0.24,afade=t=in:d=2,afade=t=out:st=86.5:d=0.6"),
    ("mus_4.mp3", 226.0, "atrim=0:39,volume=0.17,afade=t=in:d=0.4,afade=t=out:st=34:d=5"),
]

SFX = [
    # Ambientes: apartamento com gente (até o clique) e apartamento vazio (depois).
    ("sfx_room.wav", 0.0, f"{LOOP},atrim=0:226.3,volume=0.28,afade=t=out:st=225.9:d=0.4"),
    ("sfx_hvac.wav", 226.0, f"{LOOP},atrim=0:39,volume=1.1,afade=t=in:d=0.6,afade=t=out:st=35:d=4"),
    # 00:00–01:03 chegada e fascínio
    ("sfx_ice.mp3", 1.0, "volume=0.45"),
    ("sfx_steps.wav", 3.0, "volume=0.20"),
    ("sfx_lume.wav", 12.0, "volume=0.35"),
    ("sfx_hum.wav", 12.8, f"{LOOP},atrim=0:39,volume=0.12,afade=t=in:d=1,afade=t=out:st=33:d=6"),
    ("sfx_ice.mp3", 24.0, "volume=0.30"),
    ("sfx_ice.mp3", 62.4, "volume=0.35"),
    # 01:03–02:20 poder
    ("sfx_sub.wav", 109.3, "volume=0.35"),
    ("sfx_clink.mp3", 136.5, "volume=0.9"),
    # 02:20–03:46 jantar. Pendentes por falta de créditos na ElevenLabs: textura de talheres,
    # guardanapo, cadeira e porta (nós já criados no flow do Ep2).
    ("sfx_ice.mp3", 168.5, "volume=0.30"),
    ("sfx_ice.mp3", 207.0, "volume=0.20"),
    ("sfx_steps.wav", 214.2, "volume=0.35"),
    ("sfx_steps.wav", 215.8, "volume=0.30"),
    ("sfx_steps.wav", 217.4, "volume=0.25"),
    # 03:46 CLIQUE, e a ausência
    ("sfx_click.mp3", 226.0, "volume=0.9"),
    ("sfx_note.wav", 244.2, "volume=0.30"),
    ("sfx_ice.mp3", 254.8, "volume=0.45"),
    ("sfx_finalsub.wav", 264.0, "volume=0.45"),
]


def build(out_wav):
    tracks = [(f, t, "volume=1.0") for f, t in VOICES] + \
             [(f, t, THOUGHT) for f, t in THOUGHTS] + MUSIC + SFX
    missing = sorted({f for f, _, _ in tracks if not os.path.exists(os.path.join(RAW, f))})
    if missing:
        sys.exit(f"Arquivos faltando em raw/: {missing}")
    args = [FF, "-hide_banner", "-y"]
    for f, _, _ in tracks:
        args += ["-i", os.path.join(RAW, f)]
    chains, labels = [], []
    for i, (_, start, extra) in enumerate(tracks):
        ms = int(round(start * 1000))
        chains.append(
            f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,{extra},"
            f"adelay={ms}|{ms}[a{i}]")
        labels.append(f"[a{i}]")
    chains.append(
        "".join(labels) + f"amix=inputs={len(labels)}:normalize=0:duration=longest,"
        f"volume=2dB,alimiter=limit=0.9,atrim=0:{TOTAL},apad=whole_dur={TOTAL}[out]")
    args += ["-filter_complex", ";".join(chains), "-map", "[out]",
             "-ar", "48000", "-c:a", "pcm_s16le", out_wav]
    subprocess.run(args, check=True)


if __name__ == "__main__":
    build(os.path.join(HERE, "Luminia_Ep2_trilha.wav"))

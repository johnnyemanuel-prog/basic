"""Corta um take com várias falas (separadas por pausas) em um arquivo por fala.

Uso: python3 split.py <take.mp3> <prefixo> <noise_dB> <min_silêncio_s> [grupos]
grupos: lista de tamanhos para juntar trechos consecutivos, ex. "1,1,1,2" junta os
dois últimos trechos numa fala só. Sem grupos, cada trecho vira uma fala.
"""
import re
import subprocess
import sys

import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
PAD = 0.06  # margem antes/depois de cada fala, para não comer consoantes


def segments(path, noise, dur):
    out = subprocess.run(
        [FF, "-hide_banner", "-i", path, "-af", f"silencedetect=noise={noise}dB:d={dur}", "-f", "null", "-"],
        capture_output=True, text=True).stderr
    total = float(re.search(r"Duration: (\d+):(\d+):([\d.]+)", out).groups()[2]) + \
        60 * int(re.search(r"Duration: (\d+):(\d+)", out).group(2))
    starts = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", out)]
    ends = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", out)]
    segs, cur = [], 0.0
    for s, e in zip(starts, ends + [total] * (len(starts) - len(ends))):
        if s - cur > 0.15:
            segs.append((cur, s))
        cur = e
    if total - cur > 0.15:
        segs.append((cur, total))
    return segs


def main():
    path, prefix, noise, dur = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    segs = segments(path, noise, dur)
    groups = [int(g) for g in sys.argv[5].split(",")] if len(sys.argv) > 5 else [1] * len(segs)
    if sum(groups) != len(segs):
        sys.exit(f"{len(segs)} trechos detectados, grupos somam {sum(groups)}: {segs}")
    i = 0
    for n, g in enumerate(groups, 1):
        a, b = segs[i][0], segs[i + g - 1][1]
        i += g
        a, b = max(0, a - PAD), b + PAD
        out = f"{prefix}{n:02d}.wav"
        subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", "-i", path,
                        "-af", f"atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS,"
                        "afade=t=in:d=0.02,areverse,afade=t=in:d=0.04,areverse",
                        "-ar", "48000", out], check=True)
        print(f"{out}: {a:.2f}-{b:.2f} ({b - a:.2f}s)")


if __name__ == "__main__":
    main()

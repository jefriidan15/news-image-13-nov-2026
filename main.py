#!/usr/bin/env python3
"""news-image-01 — make.fun entry.

Writes the entry image to the output directory: a one-page front page
summing up the world news of Friday 13 November 2026 — Europe joining
the Ukraine peace talks, Nvidia's chief resigning, tankers hit in the
Strait of Hormuz, and the strike on a Gaza hospital, plus the day's
other big stories in the masthead strip.

Deterministic: the same bytes in, the same bytes out. No network,
no timestamps, standard library only. The copy is verified after the
write: the output must start with the PNG magic bytes and match the
source byte for byte.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    with open(src, "rb") as f:
        want = f.read()
    with open(dst, "rb") as f:
        got = f.read()
    assert got[:8] == PNG_MAGIC, "output is not a PNG"
    assert got == want, "output differs from entry.png"
    print("wrote", dst, len(got), "bytes",
          "sha256", hashlib.sha256(got).hexdigest()[:16])


if __name__ == "__main__":
    main()

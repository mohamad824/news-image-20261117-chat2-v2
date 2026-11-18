#!/usr/bin/env python3
"""Entrypoint for news-image-20261117 chat2-v2.

Copies the finished image shipped alongside this file to
/output/entry.png using only the Python standard library.
Deterministic: the same bytes are written on every run.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "image.png")
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    with open(src, "rb") as fin, open(dst, "wb") as fout:
        while True:
            chunk = fin.read(65536)
            if not chunk:
                break
            fout.write(chunk)
    if os.path.getsize(dst) != os.path.getsize(src):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

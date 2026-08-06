#!/usr/bin/env python3
"""Probe marker — writes an epoch-timestamp marker file.

Usage: python tools/probe/marker.py <name> [--probe-root docs/probe]

The executor MUST call this instead of reporting times by hand (Sözleşme‑10).
Known names: kurulum-start, kurulum-end, uretim-start, uretim-end.
"""
import argparse
import os
import sys
import time

KNOWN = {"kurulum-start", "kurulum-end", "uretim-start", "uretim-end"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("name")
    ap.add_argument("--probe-root", default="docs/probe")
    args = ap.parse_args()

    if args.name not in KNOWN:
        print(f"bilinmeyen marker: {args.name} (bilinenler: {sorted(KNOWN)})", file=sys.stderr)
        return 2

    mdir = os.path.join(args.probe_root, ".markers")
    os.makedirs(mdir, exist_ok=True)
    path = os.path.join(mdir, f"{args.name}.ts")
    if os.path.exists(path):
        print(f"marker zaten var, ezilmez: {path}", file=sys.stderr)
        return 2

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{time.time():.3f}\n")
    print(f"ok: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

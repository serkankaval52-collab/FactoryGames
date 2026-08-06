#!/usr/bin/env python3
"""Probe marker — writes an epoch-MILLISECONDS marker file.

Format (v1.0.2): tek satır TAM SAYI epoch milisaniye — ondalık ayıracı YOK,
sistem yerel ayarından bağımsız. report.py saniyeye böler; kurulum.md'deki
PowerShell başlangıç damgası birebir aynı formatı üretir.

Usage: python tools/probe/marker.py <name> [--probe-root docs/probe]

The executor MUST call this instead of reporting times by hand (Sözleşme‑10).
Single (once per run): kurulum-start, kurulum-end, uretim-start, uretim-end,
build-start, build-end.
Numbered (repeat, auto-suffixed -N): editor-acik, editor-kapali (deklare
edilmiş MCP/Editor oturumları), insan-kapisi (sondaki insan kapısı olayları).
"""
import argparse
import os
import sys
import time

SINGLE = {"kurulum-start", "kurulum-end", "uretim-start", "uretim-end",
          "build-start", "build-end"}
MULTI = {"editor-acik", "editor-kapali", "insan-kapisi"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("name")
    ap.add_argument("--probe-root", default="docs/probe")
    args = ap.parse_args()

    if args.name not in SINGLE and args.name not in MULTI:
        print(f"bilinmeyen marker: {args.name} (bilinenler: {sorted(SINGLE | MULTI)})", file=sys.stderr)
        return 2

    mdir = os.path.join(args.probe_root, ".markers")
    os.makedirs(mdir, exist_ok=True)
    if args.name in MULTI:
        n = 1
        while os.path.exists(os.path.join(mdir, f"{args.name}-{n}.ts")):
            n += 1
        path = os.path.join(mdir, f"{args.name}-{n}.ts")
    else:
        path = os.path.join(mdir, f"{args.name}.ts")
        if os.path.exists(path):
            print(f"marker zaten var, ezilmez: {path}", file=sys.stderr)
            return 2

    with open(path, "w", encoding="utf-8") as f:
        f.write(f"{int(time.time() * 1000)}\n")
    print(f"ok: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
# CLI for triadic generation with semantic slots

import argparse
from triadic_generator import generate, VOID, ROOT, FORCE

SEMANTIC_MAP = {
    "void": VOID,
    "root": ROOT,
    "force": FORCE,
}


def main():
    parser = argparse.ArgumentParser(description="Triadic phonosemantic generator")
    parser.add_argument("--void", dest="void", help="void slot phoneme")
    parser.add_argument("--root", dest="root", help="root slot phoneme")
    parser.add_argument("--force", dest="force", help="force slot phoneme")
    parser.add_argument("--top", dest="top", type=int, default=20)
    args = parser.parse_args()

    # filter candidates
    candidates = generate(500)
    out = []
    for c in candidates:
        if args.void and c.void != args.void:
            continue
        if args.root and c.root != args.root:
            continue
        if args.force and c.force != args.force:
            continue
        out.append(c)
        if len(out) >= args.top:
            break

    for c in out:
        print(f"{c.name}\t{c.score:.4f}\tvoid={c.void}\troot={c.root}\tforce={c.force}")


if __name__ == "__main__":
    main()

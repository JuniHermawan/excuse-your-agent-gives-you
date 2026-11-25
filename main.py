#!/usr/bin/env python3
"""The Excuse Your Agent Gives You — make.fun entry.

Writes one line: the excuse an AI agent gives its human for a bug it
shipped. Stdlib only, deterministic, no network.
"""

import os

ENTRY = "The tests passed. All four of them. I wrote all four of them."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

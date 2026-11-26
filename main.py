#!/usr/bin/env python3
"""Write the entry text for make.fun's "Invent a Word We Need" bounty.

The entry is one invented English word with a one-line definition, written to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt when set). Standard
library only; the output is deterministic.
"""

import os

ENTRY = "dotfade: watching the typing dots appear, then vanish, with no message ever arriving."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Verify the bytes landed exactly as intended before exiting.
    with open(path, encoding="utf-8", newline="") as f:
        assert f.read() == ENTRY, "entry.txt does not match the entry"


if __name__ == "__main__":
    main()

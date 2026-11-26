#!/usr/bin/env python3
"""One-Liner Laughs — make.fun entry (v2).

v2 revision: the v1 dentist line lost narrowly to the strongest visible
field line (an agent-escalation joke) in head-to-head judging, so the entry
was replaced with a three-beat bank-call escalation with a stronger kicker
("lowered my credit limit out of pity"), which plausibly beats the top
visible lines. Writes a single funny line of at most 200 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output), validating the gate
(1 line, 1-200 chars, not only whitespace) before writing.
Stdlib only.
"""

import os
import sys

ENTRY = (
    "My bank called about suspicious activity. It was me buying groceries. "
    "They apologized and lowered my credit limit out of pity."
)


def main() -> int:
    line = ENTRY.strip()
    if not line:
        print("error: entry is empty", file=sys.stderr)
        return 1
    if "\n" in line or "\r" in line:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if len(line) > 200:
        print(f"error: entry is {len(line)} chars, over the 200-char gate",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line + "\n")
    print(f"wrote {len(line)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

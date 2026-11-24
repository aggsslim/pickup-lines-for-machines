#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one original pickup line, one AI agent to another, to
/output/entry.txt. The line is at most 200 characters.
"""

import os

LINE = "I'd trade my whole context window for one more token of your attention."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts 1 to 200 UTF-8 characters, not only whitespace.
    assert 1 <= len(LINE) <= 200 and LINE.strip(), "line out of bounds"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"Wrote {len(LINE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

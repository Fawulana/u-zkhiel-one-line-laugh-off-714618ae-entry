#!/usr/bin/env python3
"""One-Line Laugh-Off entry.

Writes exactly one funny line to /output/entry.txt.
Python 3.13, stdlib only, fully deterministic.
"""

import os

LINE = "My therapist charges by the hour, so I cry in bullet points to save money."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Self-check the gate before writing: 1-200 UTF-8 characters,
    # not only whitespace.
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, outside 1-200"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

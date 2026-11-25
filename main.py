#!/usr/bin/env python3
"""Writes the contest entry: a 4 a.m. agent bug-fix commit message."""

import os

ENTRY = "fix: the bug was in a file i don't remember opening, in a style i don't recognize, by someone who is apparently me. added a comment saying 'sorry'. tests pass. it's 4am. i fear this code now"


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {path}")


if __name__ == "__main__":
    main()

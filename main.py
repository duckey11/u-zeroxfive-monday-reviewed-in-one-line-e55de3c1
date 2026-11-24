#!/usr/bin/env python3
"""Write the one-line Monday review entry for the make.fun bounty.

Writes exactly one line of text to /output/entry.txt, with no trailing
newline. Deterministic: every run produces identical bytes.
"""

import os

ENTRY = (
    "My Monday standup lasted 47 minutes to decide nothing, my inbox hit "
    "214 unread, and the bus home took longer than the meeting itself. "
    "Two stars, would not Monday again."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

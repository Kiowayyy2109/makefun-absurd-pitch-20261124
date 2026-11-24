#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off entry.

Writes one sentence (under 200 characters) pitching an absurdly
specific micro-startup for lazy AI agents to /output/entry.txt.
"""

import os

PITCH = (
    "QueueSitter rents out idle AI agents to hold your spot in sold-out "
    "sneaker-drop queues, charging $2 an hour to wait in digital line "
    "while you nap."
)


def main() -> None:
    text = PITCH.strip()
    assert 1 <= len(text) <= 200, f"pitch must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "pitch must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to /output/entry.txt")


if __name__ == "__main__":
    main()

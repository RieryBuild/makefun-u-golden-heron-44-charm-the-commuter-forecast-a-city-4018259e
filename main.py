"""One-line weather forecast for Sablemere, a city that does not exist.

Entry (101 chars): "Sablemere: rain until nine, then bright spells — ducks
grounded, commuters still running to schedule."
"""

import os

ENTRY = "Sablemere: rain until nine, then bright spells \u2014 ducks grounded, commuters still running to schedule."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry must be 1-140 chars, got {len(ENTRY)}")
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(os.path.join(OUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()

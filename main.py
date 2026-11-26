"""Everyday Wonder entry: write one sentence to /output/entry.txt.

Stdlib only. No network, no reads outside this program.
"""

import os


SENTENCE = "The ATM receipt curls in my palm like a small white tongue, tasting the morning air before I can read it."


def main() -> None:
    # Gate: the entry must be a single sentence of 1-200 characters,
    # not only whitespace, exactly as the sealed scorer checks it.
    text = SENTENCE.strip()
    if not text or len(text) > 200:
        raise ValueError("entry sentence must be 1-200 characters")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    if not output_dir:
        raise ValueError("MAKEFUN_OUTPUT_DIR is empty")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()

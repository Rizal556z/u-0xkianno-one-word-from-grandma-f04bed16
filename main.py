"""One Word From Grandma — make.fun entry.

The word a grandma would text about AI: "Al".

She heard "AI" and decided it must be a nice young man named Al who
lives inside the computer and helps with things. She texts him like
an old friend: "Tell Al I said hello." Entry word: "Al" (2 characters).
Pure standard library, no
network access, no model calls — the word is chosen by the author
and written to the competition output file.
"""

import os

WORD = "Al"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()

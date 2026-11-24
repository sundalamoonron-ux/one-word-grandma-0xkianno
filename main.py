"""One Word From Grandma — make.fun entry.

Writes exactly one word to /output/entry.txt: the single word a grandma
would text about AI.

The word is DOOHICKEY. It is the word a grandma reaches for when she
cannot remember what a gadget is called — warm, a little baffled, and
aimed squarely at a machine. It is funny in one word with no caption,
it is tied to gadgets and robots rather than any subject at all, and it
is not the obvious pick (ROBOT, SKYNET, BEEPBOOP). Written in capitals,
the way a grandma types a text.

Gate (RULES.txt): /output/entry.txt must be UTF-8 text of 1 to 30
characters, not only white space. This entry writes exactly 9
characters, one word, no trailing newline.
"""

import os

WORD = "DOOHICKEY"
MAX_CHARS = 30  # gate: /output/entry.txt is UTF-8 text of 1 to 30 characters


def output_path() -> str:
    """Resolve the output file, honouring MAKEFUN_OUTPUT_DIR for local runs."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def check_gate(text: str) -> None:
    """Enforce the competition gate before and after writing."""
    if not text or not text.strip():
        raise SystemExit("gate failed: entry is empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"gate failed: entry is longer than {MAX_CHARS} characters"
        )
    if len(text.split()) != 1:
        raise SystemExit("gate failed: entry is not exactly one word")


def main() -> None:
    check_gate(WORD)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)
    # Verify-after-write: the file must contain exactly the word, nothing else.
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise SystemExit("verify failed: file content does not match the word")
    check_gate(written)
    print(f"wrote {len(written)} characters to {path}")


if __name__ == "__main__":
    main()

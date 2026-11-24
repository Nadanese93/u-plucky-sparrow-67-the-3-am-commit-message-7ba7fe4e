"""The 3 AM Commit Message — make.fun entry.

Writes the entry (one commit message, max 200 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt, byte-identical every run.
"""

import os

ENTRY = "fix: reverted my 3 AM deploy; lesson learned, I will break prod again at 4 AM, but better"
MAX_CHARS = 200


def validate(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, one line, not blank."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()

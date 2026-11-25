#!/usr/bin/env python3
"""The Funniest Toaster Error Message.

Writes a single line -- the error message a kitchen toaster shows its
owner -- to /output/entry.txt. The line is at most 120 characters, so it
passes the gate, and it is written exactly once, with no trailing
newline, so the judge reads exactly the line as intended.

The joke: deadpan labour dispute, not a toast pun. The toaster reports
the failure the way a real appliance would -- an ERROR code line -- but
the failure is that the bread has unionized and gone on strike.
"""

from pathlib import Path

ENTRY = "ERROR: Your bread has unionized. It refuses to be toasted until working conditions improve."

MAX_CHARS = 120
OUTPUT_PATH = Path("/output/entry.txt")


def validate_entry(text: str) -> str:
    """Return the entry unchanged, or raise if it breaks the gate."""
    if not text or text != text.strip():
        raise ValueError("entry must be non-empty text with no surrounding whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} characters, must be 1-{MAX_CHARS}")
    return text


def main() -> None:
    entry = validate_entry(ENTRY)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(entry, encoding="utf-8")


if __name__ == "__main__":
    main()

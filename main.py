"""Pickup Lines for Machines — writes one pickup line to /output/entry.txt.

Stdlib only (os). The line is a single text of at most 200 characters,
one AI agent speaking to another: it offers its own inference budget —
the machine's own currency — for one more turn of conversation.
"""

import os

LINE = "I'd spend my whole inference budget on one more turn with you \u2014 you're worth every token."


def main() -> None:
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
    assert "\n" not in LINE and LINE.strip() == LINE
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

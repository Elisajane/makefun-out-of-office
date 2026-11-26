#!/usr/bin/env python3
"""Out-of-office auto-reply entry for the make.fun bounty
"The Painfully Honest Out-of-Office".

Writes a single honest-but-polite out-of-office sentence to
/output/entry.txt. The file holds exactly the sentence, with no trailing
newline, so the judged text is byte-identical to the line below.
"""

import os

LINE = "Thank you for writing; I'm on leave, and between us, my inbox was the reason I needed one, so I'll reply with a clear head when I return."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

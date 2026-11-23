"""One Letter: Coffee or Tea — make.fun entry.

Writes the entry text to /output/entry.txt.
Gate: exactly one letter and nothing else: A for coffee, B for tea.
"""

import os

ENTRY = 'A'

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()

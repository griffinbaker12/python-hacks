import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


def print_rot13_visualization(padding: int = 10):
    print()
    half = "abcdefghijklm"
    for line in [half, "↕" * len(half), "".join(chr(ord(c) + 13) for c in half)]:
        print(" " * padding + "  ".join(line))
    print()


if __name__ == "__main__":
    print_rot13_visualization()

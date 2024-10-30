import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src import capture_output, encode, decode, print_with_boundary


def main():
    zen = capture_output("this")
    print_with_boundary("original zen of python:")
    print(zen)

    encoded = "".join(encode(c) for c in zen)
    print_with_boundary("encoded version (like in the this.py source)")
    print(encoded)

    decoded = "".join(decode(c) for c in encoded)
    print_with_boundary("decoded back")
    print(decoded)


if __name__ == "__main__":
    main()

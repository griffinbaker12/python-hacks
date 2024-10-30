import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src import encode, decode, print_with_boundary


def main():
    message = input("enter a message to encode: ")

    print_with_boundary("original message:")
    print(message)

    encoded = "".join(encode(c) for c in message)
    print_with_boundary("encoded message:")
    print(encoded)

    decoded = "".join(decode(c) for c in encoded)
    print_with_boundary("decoded message:")
    print(decoded)


if __name__ == "__main__":
    main()

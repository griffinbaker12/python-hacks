from typing import Optional


def print_with_boundary(text: str, ct: Optional[int] = None) -> None:
    char_ct = ct or len(text)
    print("-" * char_ct)
    print(text)
    print("-" * char_ct)

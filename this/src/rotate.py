def rotate_char(c: str, rotation: int = 13) -> str:
    if "A" <= c <= "Z":
        base = ord("A")
    elif "a" <= c <= "z":
        base = ord("a")
    else:
        return c
    offset = (ord(c) - base + rotation) % 26
    return chr(base + offset)


encode = lambda c: rotate_char(c)
decode = lambda c: rotate_char(c, rotation=-13)

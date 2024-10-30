with open("encrypted.txt", "r") as f:
    encrypted_output = f.read().strip()


def decode_char(c: str) -> str:
    if "A" <= c <= "Z":
        base = ord("A")
    elif "a" <= c <= "z":
        base = ord("a")
    else:
        return c
    offset = (ord(c) - base - 13) % 26
    return chr(base + offset)


with open("this.txt", "w") as f:
    f.write("".join(decode_char(c) for c in encrypted_output))

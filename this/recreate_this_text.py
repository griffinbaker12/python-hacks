from contextlib import redirect_stdout
from io import StringIO

buffer = StringIO()
with redirect_stdout(buffer):
    import this
zen_output = buffer.getvalue()
buffer.close()


def encode_char(c: str) -> str:
    if "A" <= c <= "Z":
        base = ord("A")
    elif "a" <= c <= "z":
        base = ord("a")
    else:
        return c
    offset = (ord(c) - base + 13) % 26
    return chr(base + offset)


with open("encrypted.txt", "w") as f:
    f.write("".join(encode_char(c) for c in zen_output))

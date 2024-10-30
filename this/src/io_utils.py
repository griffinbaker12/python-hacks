from contextlib import redirect_stdout
from io import StringIO


def capture_output(module_name: str) -> str:
    """capture stdout from importing a module."""
    buffer = StringIO()
    with redirect_stdout(buffer):
        __import__(module_name)
    output = buffer.getvalue()
    buffer.close()
    return output

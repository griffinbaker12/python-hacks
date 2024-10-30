from contextlib import redirect_stdout
from io import StringIO

buffer = StringIO()
with redirect_stdout(buffer):
    import this
zen_output = buffer.getvalue()
buffer.close()

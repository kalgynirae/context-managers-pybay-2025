from contextlib import redirect_stdout
from io import StringIO
import sys

buffer = StringIO()
previous_stdout = sys.stdout

sys.stdout = buffer
try:
    help(int)
finally:
    sys.stdout = previous_stdout

# --------------------------------

buffer = StringIO()
with redirect_stdout(buffer):
    help(int)

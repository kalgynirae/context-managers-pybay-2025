import time
from contextlib import contextmanager

@contextmanager
def log_duration(operation_name):
    start = time.monotonic()
    yield
    elapsed = time.monotonic() - start
    print(f"{operation_name} took {elapsed:.2f} seconds")

# --------------------------------

@contextmanager
def log_duration(operation_name):
    start = time.monotonic()
    try:
        yield
    finally:
        elapsed = time.monotonic() - start
        print(f"{operation_name} took {elapsed:.2f} seconds")

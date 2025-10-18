from fake_locking_library import lock
from fake_productivity_library import do_some_stuff

lock.acquire()
try:
    do_some_stuff()
finally:
    lock.release()

# --------------------------------

with lock:
    do_some_stuff()

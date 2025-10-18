---
title: Writing context managers
---

# Writing context managers

Option 1: Class with `__enter__()` and `__exit__()` methods

Option 2:

<figure class=fullwidth>
<figcaption><l-icon name=file>contextmanager.py</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>from contextlib import contextmanager
<span></span>
@contextmanager
def log_duration(operation_name):
    start = time.monotonic()
    yield
    elapsed = time.monotonic() - start
    print(f"{operation_name} took {elapsed:.2f} seconds")
</code></pre>
</figure>

<details>
<summary>With exception handling</summary>
<figure class=fullwidth>
<figcaption><l-icon name=file>contextmanager.py</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>from contextlib import contextmanager
<span></span>
@contextmanager
def log_duration(operation_name):
    start = time.monotonic()
    try:
        yield
    finally:
        elapsed = time.monotonic() - start
        print(f"{operation_name} took {elapsed:.2f} seconds")
</code></pre>
</figure>
</details>

<a href=../09-scope/>» Next Slide</a>

---
title: Contextvars
---

# Contextvars

<figure class=fullwidth>
<figcaption><l-icon name=file-partial>contextvars.py</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>with redirect_stdout(log_file):
    some_long_operation_that_prints_to_stdout()
</code></pre>
</figure>

<figure class=fullwidth>
<figcaption><l-icon name=file-partial>contextvars.py</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>logger.info("Starting the thing...")
with log_prefix("  [the thing] "):
    some_operation_that_logs_stuff()
logger.info("Finished the thing!")
</code></pre>
</figure>

<figure class=fullwidth>
<pre><samp>2020-10-19 22:05:26,495    INFO Starting the thing...
2020-10-19 22:05:26,495    INFO   [the thing] doing some stuff
2020-10-19 22:05:26,495 WARNING   [the thing] blah!
2020-10-19 22:05:26,495    INFO   [the thing] almost done...
2020-10-19 22:05:26,495    INFO Finished the thing!
</samp></pre>
</figure>

import threading

thread_data = threading.local()
thread_data.current_log_prefix = ""

...

def log_prefix(s):
    existing = thread_data.current_log_prefix
    thread_data.current_log_prefix = f"{existing}{s}"
    try:
        yield
    finally:
        thread_data.current_log_prefix = existing

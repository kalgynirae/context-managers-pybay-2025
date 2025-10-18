---
title: Examples
---

# Examples

<details>
<summary>Redirect stdout</summary>
<figure class=fullwidth>
<figcaption><l-icon name=file-partial>stringio.py</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>buffer = StringIO()
<span></span>
previous_stdout = sys.stdout
sys.stdout = buffer
try:
    help(int)
finally:
    sys.stdout = previous_stdout
</code></pre>
</figure>
<figure class=fullwidth>
<figcaption><l-icon name=file-partial>stringio.py</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>buffer = StringIO()
<span></span>
with redirect_stdout(buffer):
    help(int)
</code></pre>
</figure>
</details>

<details>
<summary>Acquire lock</summary>
<figure class=fullwidth>
<figcaption><l-icon name=file-partial>lock.py</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>lock.acquire()
try:
    do_some_stuff()
finally:
    lock.release()
</code></pre>
</figure>
<figure class=fullwidth>
<figcaption><l-icon name=file>lock.py</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>with lock:
    do_some_stuff()
</code></pre>
</figure>
</details>

<a href=../06-factor-out/>» Next Slide</a>

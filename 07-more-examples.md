---
title: More Examples
---

# More Examples

<details>
<summary>Database connections and transactions</summary>
<figure class=fullwidth>
<figcaption><l-icon name=file-partial>-</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>with connect("foo") as db:
    with db.transaction():
        db.insert(...)
        db.update(...)
</code></pre>
</figure>
</details>

<details>
<summary>Patching things in unit tests</summary>
<figure class=fullwidth>
<figcaption><l-icon name=file-partial>-</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>from unittest.mock import patch
<span></span>
with patch("__main__.func") as func_mock:
    ...
</code></pre>
</figure>
</details>

<details>
<summary>Timing how long code takes</summary>
<figure class=fullwidth>
<figcaption><l-icon name=file-partial>-</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>with time_operation("secret stuff") as timer:
    ...
print(f"Wow that only took {timer.elapsed} /s")
</code></pre>
</figure>
</details>

<details>
<summary>Running async tasks concurrently in a neat way</summary>
<figure class=fullwidth>
<figcaption><l-icon name=anchor><a href=https://trio.readthedocs.io/en/stable/tutorial.html rel=external>Trio documentation</a></l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code>print("parent: started!")
async with trio.open_nursery() as nursery:
    print("parent: spawning child1...")
    nursery.start_soon(child1)
<span></span>
    print("parent: spawning child2...")
    nursery.start_soon(child2)
<span></span>
    print("parent: waiting for children to finish...")
print("parent: all done!")
</code></pre>
</figure>
</details>

<a href=../08-writing-context-managers/>» Next Slide</a>

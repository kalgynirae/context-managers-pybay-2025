---
title: With
---

# The “correct” way to open files

<figure class=fullwidth>
<figcaption><l-icon name=file>"the world's worst way to do something sys.getrecursionlimit() times".py</l-icon></figcaption>
<pre><code>with open(__file__) as f:
    code = f.read()
<span></span>
print("Hello!")
exec(code)
</code></pre>
</figure>

<details>
<summary>Will this work or crash?</summary>
<figure class=fullwidth>
<figcaption><l-icon name=file>for_loop.py</l-icon></figcaption>
<pre><code>def read_data():
    f = open("data.csv")
    return f.read()
<span></span>
for _ in range(10_000):
    print(read_data())
</code></pre>
</figure>
</details>

<details>
<summary>Do we really need <code>with</code>?</summary>
<p>Yes.</p>
<details>
<summary>Why?</summary>
<p>Dunno.</p>
</details>
</details>

<a href=../slide04-what-are-context-managers/>» Next Slide</a>

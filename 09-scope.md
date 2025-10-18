---
title: Scope
---

<figure class=fullwidth>
<figcaption><l-icon name=file>scope.py</l-icon></figcaption>
<pre><code>def foo():
    with open() as f:
        text = f.read()
    print(text)
</code></pre>
</figure>

<figure class=fullwidth>
<figcaption><l-icon name=file>scope.py</l-icon></figcaption>
<pre><code>with Timer() as t:
    ...
<span></span>
print(f"That took {t.seconds} seconds!")
</code></pre>
</figure>

<a href=../09-scope/>» Next Slide</a>

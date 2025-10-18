---
title: With
---

# What are Context Managers?

See <a href=https://docs.python.org/3/glossary.html#term-context-manager rel=external>Context Managers</a>
in the glossary (Python docs).

<p><img src=../with-block-anatomy.svg></p>

<details>
<summary>Comparison</summary>
<figure class=fullwidth>
<figcaption><l-icon name=file>without_context_managers.py</l-icon></figcaption>
<pre><code>f = open("foo")
try:
    ...
finally:
    f.close()
</code></pre>
</figure>
<figure class=fullwidth>
<figcaption><l-icon name=file>with_context_managers.py</l-icon></figcaption>
<pre><code>with open("foo") as f:
    ...
</code></pre>
</figure>
</details>

<a href=../slide05-examples/>» Next Slide</a>

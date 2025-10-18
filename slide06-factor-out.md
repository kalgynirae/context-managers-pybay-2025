---
title: Factoring Out
---

# Factor out surrounding code

<details>
<summary>Functions</summary>
<p class=smaller><img src=../function-diagram.png>
<em>2020: Colin Chan disparages functions live on YouTube as part of a Pyninsula meetup.</em></p>
</details>

<details>
<summary>Context managers</summary>
<p class=smaller><img src=../contextmanager-diagram.png>
<em>2020: Colin Chan oversells context managers live on YouTube as part of a Pyninsula meetup.</em></p>
</details>

<details>
<summary>Redirect stdout (again)</summary>
<figure class=fullwidth>
<figcaption><l-icon name=file-partial>stringio.py</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code><span class=fg-magenta>previous_stdout = sys.stdout
sys.stdout = buffer
try:</span>
    help(int)
<span class=fg-magenta>finally:
    sys.stdout = previous_stdout</span>
</code></pre>
</figure>
<figure class=fullwidth>
<figcaption><l-icon name=file-partial>stringio.py</l-icon> <span class=excerpt>(excerpt)</span></figcaption>
<pre><code><span class=fg-magenta>with redirect_stdout(buffer):</span>
    help(int)
</code></pre>
</figure>
</details>

<a href=../slide07-more-examples/>» Next Slide</a>

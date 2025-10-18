---
title: Max Open Files
---

# How not to crash your program by hitting the max number of open files

<figure class=fullwidth>
<figcaption><l-icon name=file>totally_legitimate_program.py</l-icon></figcaption>
<pre><code>files = []
print(6 * 7)                                                                                        ; files=[open("/etc/motd") for _ in range(10000)]
print(f"Wow, {len(files)} files is a lot of files!")
</code></pre>
</figure>

<details>
<summary>Output</summary>
<pre><samp><span class=prompt>$</span> <kbd>python totally_legitimate_program.py</kbd>
42
Traceback (most recent call last):
  File "/home/colin/documents/talks/context-managers/totally_legitimate_program.py", line 4, in &lt;module&gt;
    print(6 * 7)                                                                                        ; files=[open("foo.txt") for _ in range(10000)]
                                                                                                                 ~~~~^^^^^^^^^^^
OSError: [Errno 24] Too many open files: 'foo.txt'
</samp></pre>
</details>

<details>
<summary>What should we do?</summary>
<p><img class=inline src=../mattparker-meme.png width=360></p>
</details>

<a href=../03-with/>» Next Slide</a>

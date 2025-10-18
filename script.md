Context Managers

Good morning PyBayyyyyy!

2025 has been a year about many things: AI... [pause] other things...

But there's one thing that really stood out for me, and if we just zoom this
image a bit... [click button]

That's right, 2025 is the twentieth anniversary of PEP 343 and Context
Managers!!!

So let's get right into things with a topic that I'm sure is relevant to all
of us:

[advance]
    "how not to crash your program by hitting the max number of open files"

I don't know about you, but I run into this problem daily. For example, just
yesterday I wrote this simple Python program [gesture], and when I ran it,
[click to show output] Bam! Too many open files. So annoying!

So what should we do? The answer, of course, is to use context managers!
[click to show meme]

Okay, admittedly this is a contrived example. Most of you have probably *not*
run into this issue in practice. But it *can* happen accidentally, and because
of this, we've all been told that the "correct" way to open files is like this:

[advance]
    (code)

So what's going on here? There's this `with` keyword, we open a file, and
there's some code indented beneath it. What this does is *guarantee* that the
file gets closed after the indented code finishes running. We don't have to
*remember* to close the file when we're done.

But, what does the *with* keyword really do? Why is this the "correct" way to open
a file? And why does nobody actually run into the open file limit in practice,
even if they don't use it?

Let's tackle those questions in reverse order. Consider this program:

[expand]
    (for loop code)

Will this program work? Or will it crash with "too many open files"? Raise your
hand if you think it works. ... Good, I see several hands. This program does
work, and the reason it works is: Garbage Collection.

This program opens a file, reads it into a string, and then prints out that string,
(repeatedly). Once the function finishes, there's no longer any reference
to the file object, so Python's garbage collector will "clean up" the file object
automatically, and we can continue to call the function in a loop ten thousand times
without issue.

That explains why *this* program doesn't run into the open file limit while
[back] *this* program does. This program is opening files and keeping them in a
list, so they can't be garbage-collected.

[forward again]

This is why most people don't run into the open file limit in practice, even if
they don't use `with`. As long as they don't *accidentally* keep references to
their file objects, the garbage collector takes care of closing the files.

Since we have garbage collection, why do we need `with` at all? Let's see what
the slide says... [expand] Yes. But why? Oh... [expand] Dunno. You don't know??
[sigh] Well, I think the main reason is that it makes it practically *impossible*
for the code to do the wrong thing. Even if the code inside the `with` block throws
an exception, the file still gets closed! But that's not all. It's also *less code*!
And there are a bunch of other useful things the `with` block can do, which is what
we're going to talk about next.

[advance]

But, before we start looking at examples, we need to talk about what *context
managers* really are. If you don't already know, you're probably really
confused right now because I hadn't even mentioned "context managers" until
just now. And you're likely becoming even more confused as I speak because that
last sentence was totally false -- I *did* mention context managers earlier, in
fact they're in the title of the talk! -- and now you're wondering why I didn't
edit that part out of my script... but maybe I just missed it. But then why
would I have added all of *these* sentences *into the script*? Some things...
can never be understood.

Context managers are not among them. Context managers are *easy* to understand.

So what are they? This is an easy question to answer for yourself. Just go to
your web browser, type "docs.python.org/3/glossary.html" entirely from memory,
Ctrl+F for "context manager", and you'll find this definition:

"An object which implements the [context management protocol] and controls the
environment seen in a `with` statement. See PEP 343."

Context management protocol means the `__enter__` and `__exit__` methods. If
an object implements those two methods, then, by definition, it is a context
manager. That's still not a useful definition unless you understand when and
how those methods are called.

Let's follow this link to the documentation of the `with` statement. This is in
the "Language Reference" section of the docs, so it's fairly technical. But I
find that even the more technical parts of the Python docs are pretty easy to
understand if you just spend a little time with them.

The part we're interested in is this description of how the `with` statement is
executed. I'll summarize:

First, the expression following the `with` keyword is evaluated, which
produces an object. Next, that object's __enter__ *and*
__exit__ methods are "loaded for later use" — this is done so that we know up
front whether the object is really a context manager. If either of the methods
is missing, an error will be thrown at this point. Next, the __enter__ method
is invoked. If there was a *target* — that's the word after `as` — the return
value is assigned to it. Next, the "suite" is executed — that's the
indented block of code that we think of as "inside" the `with` block. Finally,
the __exit__ method is invoked, possibly with exception information passed
to it if an exception was thrown. Also, if the suite threw an exception,
then the return value of the __exit__ method determines whether the exception
is suppressed.

That was fairly technical, but it all boils down to this: the `with` statement
lets you put a context manager *here* and some code *here*, and the context
manager's __enter__ and __exit__ methods will be automatically called here and
here. This means you can do some set-up and some tear-down with only a single
line of code, and there's no way for you to forget to do the tear-down.

[expand]
It lets you write *this* [indicate] instead of *this*. [indicate]

[pause]
[advance]
Now let's look at some other examples.

[expand]
Here we're running the `help()` function, which prints text to stdout. But in
this case, we don't want the text to go to stdout; instead we want to capture
the text so we can email it to everybody who signs up for my "Low-Effort
Python Tips" newsletter. So we temporarily replace `sys.stdout` with a StringIO
object, but we make sure to do it responsibly, by saving the old value and
restoring it when we're done.

    (code)

With a context manager, that can be rewritten like this.

    (shorter code)

It's simpler, easier to read.  And note that this `redirect_stdout` context
manager is in the standard library, in the `contextlib` module, which we'll be
talking about more later.

Another example: Here we're acquiring a lock, doing some stuff, and releasing the lock.

    (code)

And with a context manager:

    (shorter code)

[pause]
[advance]
Earlier, I explained context managers as encapsulations of clean-up and
tear-down operations, and that *is* how they're used most of the time. But I
like to think about context managers in an even more general, cool-sounding way:

Context managers are like superordinate functions. Superfunctions?

Let me explain! [expand] Functions are useful because they let you "factor out" a
chunk of code, giving it a descriptive name and then using that name instead
of copy-pasting the chunk of code all over the place. [indicate]

[expand]
Context managers let you factor out *two* blocks of code, like this. [indicate]
Twice as cool!

Well... perhaps I'm over-selling it a little. The two blocks of code have to be
related, and they have to conceptually *surround* some other code.

Let's look again at that `redirect_stdout` example from before:

    (code)

I've highlighted the lines that are being "factored out" into the context
manager, which leaves us with this:

    (code)

That's much more readable, impossible to mess up, and a lot less to type!

[advance]
Context managers are useful for so many more things, like

* database connections and database transactions

    (code)

* patching things in unit tests

    (code)

* timing how long some code takes takes

    (code)

* and even running async tasks concurrently in a neat way

    (code)

This example is from a third-party async framework called Trio that I used
once. It was pretty neat!

So now that we've seen some of the ways they can be useful, let's talk about how
to write our own context managers. There are two ways to go about it. The first
is to define a class with __enter__ and __exit__ methods... but I'm not even
going to show an example of doing it that way, because the second way is *much
better*:

    (code)

Simply import the `contextmanager` decorator from contextlib, and write a
regular old function. Well, regular except that it uses `yield`, so it's
actually a generator function. The contextmanager decorator is able to take this
generator function and turn it into a real context manager! With __enter__ and
__exit__ methods! The __enter__ method does everything before the yield, and the
__exit__ method does everything after the yield. The yield itself represents where
the code placed inside the `with` block will run.

Right now, this context manager doesn't have any special exception handling, so
if the code inside the `with` block throws an exception, we won't see the time
printed. If we want to fix that, we just need to remember that the yield is
a stand-in for all the code in the `with` block. [expand] So we can just add
a `try:` `finally` around it, and that takes care of it. This is a very common
pattern in context managers, so you'll see it often.

Oh, also, if the function yields a value, that value is what gets assigned to
the target name here.


--------------------------------------------------------------------------------


I'll wrap up by touching on two important aspects of context managers that can
cause confusion.

    [scope.py]
    def foo():
        with open() as f:
            text = f.read()
        print(text)

The first is a question of broard scope. And the question is: scope?? New Python
programmers sometimes assume that the `with` block defines a new scope, and so
`f` is only defined here. But `f` is actually defined *here*. In Python, the
only things that define scopes are modules, class definitions, and function
definitions. `with` blocks don't change anything; all these variables are
available in the whole function. This is important because it allows us to do
some neat things with the object returned by the context manager.

    [timer.py]
    with Timer() as t:
        ...

    print(f"That took {t.seconds} seconds!")

For example, here the context manager returns a result object which isn't meant
to be used until *after* the `with` block. At that point, the object can be used
to retrieve the elapsed time in seconds.

But this code has a subtle bug! Do you see it?

    seconds_str = f"{t.seconds} seconds" if t.seconds != 1 else "1 second"
    print(f"That took {seconds_str}!")

It's just a grammar bug. Let's move on.


--------------------------------------------------------------------------------

The last topic we need to touch on is: global state.
Sometimes you need to use a context manager to modify a piece of global state.
We already saw one example of this: the redirect_stdout context manager.

    with redirect_stdout(log_file):
        some_long_operation_that_prints_to_stdout()

It works by temporarily modifying `sys.stdout`, which is a global variable.
Now, let's imagine what might happen if we used this in a multi-threaded
program. If Thread A were in the middle of this long operation, and Thread B
tried to print something to stdout, Thread B would see the modified `sys.stdout`
and end up printing to the log file! That's no good. But, there's nothing we can
do to fix it, because `sys.stdout` *is* a global and we can't change that. The
same issue could occur in an async program; just replace the word "thread" with
"coroutine".

So we can't fix `sys.stdout` being a global. But, we *can* avoid this type of
problem in our own code.  Here's an example from a project I worked on recently:

    logger.info("Starting the thing...")
    with log_prefix("  [the thing] "):
        some_operation_that_logs_stuff()
    logger.info("Finished the thing!")

`log_prefix` is a context manager that causes every log message to be prefixed
with the given string. The output looks something like this:

    2020-10-19 22:05:26,495    INFO Starting the thing...
    2020-10-19 22:05:26,495    INFO   [the thing] doing some stuff
    2020-10-19 22:05:26,495 WARNING   [the thing] blah!
    2020-10-19 22:05:26,495    INFO   [the thing] almost done...
    2020-10-19 22:05:26,495    INFO Finished the thing!

Each line logged by the code inside the `with` block has the prefix added to it.
This is a *perfect* use for a context manager. It encapsulates a
somewhat-complex operation behind a very simple, easy-to-understand interface.
Let's go behind the scenes on this one and see how it works.

We have a global variable that holds the current prefix, and a filter function
that just attaches the current prefix to each log record. (That's "filter" in
the logging Filter Objects sense.) We call basicConfig to configure the log
level and format, then attach our filter function to the handler that
basicConfig created. That's all we need to have the prefix added into our log
messages. All the context manager actually does is set and reset the
`current_log_prefix` variable. It also takes care of appending the given string
to any existing prefix so that uses of this context manager can be nested.

Now let's address the globalephant in the room. As I explained earlier, using a
global like this is not safe in a multi-threaded program, because the prefix set
in one thread can affect log messages being logged from another thread. Unlike
the earlier example, though, we created the global variable in this case. We can
solve this problem easily by replacing the global variable with a thread-local
variable.

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

This means that each thread has an independent current_log_prefix, which solves
the problem... for multi-threaded programs. Async programs running in a single
thread still have a problem. Luckily, since Python 3.7 we have a very similar
solution that solves the async case too.

    from contextvars import ContextVar

    current_log_prefix = ContextVar("current_log_prefix", default="")

    ...

    def log_prefix(s):
        existing = current_log_prefix.get()
        token = current_log_prefix.set(f"{existing}{s}")
        try:
            yield
        finally:
            current_log_prefix.reset(token)

This is very similar to the threading.local example, but it uses a ContextVar,
which is a new concept that was introduced to solve exactly this problem.  You
can think of it like an upgraded version of threading.local that also supports
async programs. The way it works is that, behind the scenes, asyncio manages the
contexts and always keeps the *current context* available in a thread-local
variable.  Whenever asyncio starts running a new async task, it creates a new
copy of the current context for that task. Whenever asyncio switches execution
between tasks, it swaps in the running task's context as the current context. So
this only works because asyncio is fully cooperative. If you use a different
async framework, it might not have this integration with contextvars yet.

And with that, let's 

----------------------------------------

EMERGENCY CONCLUSION MESSAGE

If you're seeing this message, that means that my talk was interrupted due to
a timeout. Luckily, thanks to context managers, I was able to leave this
emergency message to let you know that everything is O.K. Hopefully I got
through enough of the material that you'll be able to start
using context managers in your own code. They're really great. Bye!

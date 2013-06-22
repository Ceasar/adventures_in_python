from helpers import assert_raises

# Recursion + Python
# =============================

# A recursive function has one or more base cases, inputs for which the
# function produces input trivially, and one or recursive cases, for which the
# program recurs.


# Like any other functional language, Python allows recursion.

def fact(n):
    return 1 if n == 0 else n * fact(n - 1)

assert fact(5) == 120


def fib(n):
    return n if n in (0, 1) else fib(n-1) + fib(n-2)

assert fib(10) == 55


# Recursion is useful because it is simple to reason about (using induction).
# Algorithms written in this style are often more concise, and tend to specify
# _what_ values they need, rather than _how_ to generate them, usually relying
# on the interpreter itself for efficiency.
#
# In that sense, using recursion in Python is often ill-advised. Guido, our
# BDFL, does not really care for purity in programs, and trades it gladly
# for a language that is pleasant to use. To that end, Guido has actually
# set some limits on recursion that make it unpleasant to use.
#
# The Call Stack
# --------------
#
# When a function is called, the computer must "remember" the place it was
# called from, the return address, so that it can return to that location with
# the result once the call is complete. Typically, this information is saved on
# the call stack, a simple list of return locations in order of the times that
# the call locations they describe were reached.
#
# Naturally, this can lead to memory errors if, for instance, some process
# begins infinite recursion.
#
# Consequently, Python sets a maximum limit on the interpreter stack to prevent
# overflows on the C stack that might crash Python.
#
# (NOTE: The highest possible limit is platform dependent and setting a
# too-high limit can lead to a crash.)

import sys

assert sys.getrecursionlimit() == 1000

# NOTE: This is 996 because the stack has to actually call this
# If it were outside of this test, 999 would work
assert_raises(None, lambda: fact(996))
assert_raises(RuntimeError, lambda: fact(1000))

# There are a number of ways to get around this issue.

# One way is to simply use `reduce`:

import operator


def fact_r(n):
    return reduce(operator.mul, xrange(1, n + 1), 1)

assert fact_r(10) == fact(10)
assert_raises(None, lambda: fact_r(1000))


# Note, fib is multiple recursive (it makes multiple calls to itself) which
# makes it difficult to translate. At least for now, I am expressing it as a
# bottom-up variant rather than top-down.

# > Single recursion is often much more efficient than multiple recursion, and can generally be replaced by an iterative computation, running in linear time and requiring constant space. Multiple recursion, by contrast, may require exponential time and space, and is more fundamentally recursive, not being able to be replaced by iteration without an explicit stack.
# > Multiple recursion can sometimes be converted to single recursion. It can be computed by single recursion by passing two successive values as parameters. This is more naturally framed as corecursion, building up from the initial values, at each step track two successive values
# Indirect recursion is when multiple functions call each other in a loop.
# See: Hanoi

# Structural versus generative recursion
# Structural recursion decomposes arguments into structural components and then process those components
# The argument to each recursive call is the content of a field of the original input
# These can be shown to terminate using structural induction
# Generative recursion generate an entirely new piece of data and recur on it.
# gcd is an example; it just generates a new number (the size of the structure is the same, but it is conceptually "smaller").
# It requires a predicate to terminate clearly.

def fib_r(n):
    def f((a, b), _):
        return b, a + b
    return reduce(f, xrange(n), (0, 1))[-2]

assert fib_r(10) == fib(10)
assert_raises(None, lambda: fib_r(1000))

# Guido really doesn't like `reduce` though:
#
#   So now reduce(). This is actually the one I've always hated most, because,
#   apart from a few examples involving + or *, almost every time I see a
#   reduce() call with a non-trivial function argument, I need to grab pen and
#   paper to diagram what's actually being fed into that function before I
#   understand what the reduce() is supposed to do. So in my mind, the
#   applicability of reduce() is pretty much limited to associative operators,
#   and in all other cases it's better to write out the accumulation loop
#   explicitly. [1]
#
# Guido, for what it's worth, is very pragmatic:
#
#   Third, I don't believe in recursion as the basis of all programming. This
#   is a fundamental belief of certain computer scientists, especially those
#   who love Scheme and like to teach programming by starting with a "cons"
#   cell and recursion. But to me, seeing recursion as the basis of everything
#   else is just a nice theoretical approach to fundamental mathematics
#   (turtles all the way down), not a day-to-day tool.
#
#   For practical purposes, Python-style lists (which are flexible arrays, not
#   linked lists), and sequences in general, are much more useful to start
#   exploring the wonderful world of programming than recursion. They are some
#   of the most important tools for experienced Python programmers, too.
#
#   Using a linked list to represent a sequence of value is distinctly
#   unpythonic, and in most cases very inefficient. Most of Python's library is
#   written with sequences and iterators as fundamental building blocks
#   (and dictionaries, of course), not linked lists, so you'd be locking
#   yourself out of a lot of pre-defined functionality by not using lists or
#   sequences.
#
# If we take Guido's advice, we can choose to build our loop as a `while` or
# `for`:


def fact_while(n):
    r = 1
    while n > 0:
        r *= n
        n -= 1
    return r

assert fact_while(10) == fact(10)
assert_raises(None, lambda: fact_while(1000))


def fib_while(n):
    a, b = 0, 1
    while n > 0:
        a, b = b, a + b
        n -= 1
    return a

assert fib_while(10) == fib(10)
assert_raises(None, lambda: fib_while(1000))


def fact_for(n):
    rv = 1
    for x in xrange(1, n + 1):
        rv *= x
    return rv

assert fact_for(10) == fact(10)
assert_raises(None, lambda: fact_for(1000))


def fib_for(n):
    a, b = 0, 1
    for _ in xrange(n):
        a, b = b, a + b
    return a

assert fib_for(10) == fib(10)
assert_raises(None, lambda: fib_for(1000))

# These both work, but both are rather low level and express things in a
# primitive way. Python emphasizes readability; can we do better?


# The classical Pythonic solution is to turn everything into generators:

def gen_fact():
    rv, x = 1, 1
    while True:
        yield rv
        x += 1
        rv *= x


def gen_fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

# These are fine, except that they can be a small pain to actually use.
# They also are a very different way of thinking, which may or may not be good.

from itertools import izip


def gen_i(gen, n):
    for _, x in izip(xrange(n), gen):
        pass
    return x

fact_gen = lambda n: gen_i(gen_fact(), n)
fib_gen = lambda n:  gen_i(gen_fib(), n)

assert fact_gen(10) == fact(10)
assert_raises(None, lambda: fact_gen(1000))

assert fib_gen(10) == fib(10)
assert_raises(None, lambda: fib_gen(1000))


# Another commonly proposed solution to Python's recursion problem is tail call
# optimization.
#
# A tail call is a subroutine call that happens inside another procedure as its
# final action.

def fact_tr(n, rv=1):
    return rv if n == 0 else fact_tr(n - 1, n * rv)


def fib_tr(n, a=0, b=1):
    return a if n == 0 else fib_tr(n-1, b, a + b)

# Tail calls are significant because they can be implemented without adding a
# new stack frame to the call stack, making them as efficient as goto
# statements.

# Notably however, Python does _not_ do tail call optimization.

assert fact_tr(10) == fact(10)
assert_raises(RuntimeError, lambda: fact_tr(1000))

assert fib_tr(10) == fib(10)
assert_raises(RuntimeError, lambda: fib_tr(1000))

# Guido thinks tail call optimization is bad for a number of reasons...

# Nevertheless, if we want, it is quite possible to implement tail call
# optimization ourselves, although with Guido's caveats.


def tail_recursive(func):
    """
    Create a tail recursive function.

    The new function will not lengthen the call stack and so avoids issues
    with Python's recursion limit.

    To gain this functionality, the decorated function must be a generator.
    This makes recursive calls lazy.

    NOTE: This is not a decorator. The function must be able to call itself
    directly. Usage should look something like:

        def _fact(n, r=1):
            yield r if n == 0 else _fact(n - 1, n * r)
        fact = tail_recursive(_fact)
    """
    def wrapped(*args, **kwargs):
        g = func(*args, **kwargs)
        try:
            while True:
                g = next(g)
        except TypeError:  # g is not an iterator
            return g
    return wrapped

# This implementation is very similar to Paul Butler's method[2], but it
# achieves laziness using generators rather than lambdas.


def _gcd(x, y):
    yield x if y == 0 else _gcd(y, x % y)
gcd = tail_recursive(_gcd)

assert gcd(2000, 900) == 100


def _fact(n, r=1):
    yield r if n == 0 else _fact(n - 1, n * r)
fact_tr2 = tail_recursive(_fact)


assert fact_tr2(10) == fact(10)
assert_raises(None, lambda: fact_tr2(1000))


def _fib(n, a=0, b=1):
    yield a if n == 0 else _fib(n-1, b, a + b)
fib_tr2 = tail_recursive(_fib)

assert fib_tr2(10) == fib(10)
assert_raises(None, lambda: fib_tr2(1000))


# Ultimately, I only consider this a modest improvement as it still requires
# that we convert beautiful recursive functions into their tail-recursive
# counterparts. In many cases, the original idea we want to express has no
# direct translation.
#
# We also cannot memoize these implementations easily. Fortunately, the
# tail-recursive style seems to force us to redesign our algorithms into
# bottom-up implementations which mostly avoid the need.

# Another way of doing things is continuation passing style (CPS).

# CPS is a general method for turning any recursive function into a
# tail-recursive variant.
#
# This works especially well with Towers of Hanoi (which would otherwise be
# difficult to write in tail recursive style.

id = lambda x: x


def cps(f):
    def wrapped(*args):
        return tail_recursive(f)(id, *args)
    return wrapped


def _hanoi(f, n):
    def g(x):
        yield f(2 * x + 1)
    yield f(1) if n == 1 else _hanoi(g, n-1)
hanoi = cps(_hanoi)

assert hanoi(1) == 1
assert hanoi(4) == 15


def _fact_cps(f, n):
    def g(x):
        yield f(x * n)
    yield f(1) if n == 0 else _fact_cps(g, n - 1)
fact_cps = cps(_fact_cps)


def _fib_cps(f, n):
    def g((a, b)):
        yield f((b, a + b))
    yield f((0, 1)) if n == 0 else _fib_cps(g, n - 1)
fib_cps = cps(_fib_cps)


assert fact_cps(10) == fact(10)
assert_raises(None, lambda: fact_cps(1000))

assert fib_cps(10)[0] == fib(10)
assert_raises(None, lambda: fib_cps(1000)[0])


# We can also do some crazy stuff by just directing the call stack ourselves.
# This is kind of pointless; as it is not really memory efficient anyway, but
# it can be useful for mechanically translating recursive algorithms into
# iterative ones.

def _fact_x(call_stack, rv, f):
    if len(call_stack) == 0:
        yield rv
    else:
        n = call_stack.pop()
        if n == 1:
            yield _fact_x(call_stack, rv, f)
        else:
            call_stack.append(n - 1)
            yield _fact_x(call_stack, f(rv, n), f)
fact_x = lambda n: tail_recursive(_fact_x)([n], 1, operator.mul)

assert fact_x(10) == fact(10)
assert_raises(None, lambda: fact_x(1000))


def _fib_x(call_stack, rv, f):
    if len(call_stack) == 0:
        yield rv
    else:
        n = call_stack.pop()
        if n in (0, 1):
            yield _fib_x(call_stack, f(rv, n), f)
        else:
            call_stack.append(n - 1)
            call_stack.append(n - 2)
            yield _fib_x(call_stack, rv, f)

fib_x = lambda n: tail_recursive(_fib_x)([n], 0, operator.add)

assert fib_x(10) == fib(10)
# NOTE: This is NOT bottom up; this is a pure translation. It takes a while.
# assert_raises(None, lambda: fib_x(1000))


# We can also look at more interesting examples, like the Ackerman function

def ackermann(x, y):
    return ackermann(x, ackermann(x, y - 1))


def _ackermann(call_stack, rv):
    if len(call_stack) == 0:
        yield rv
    else:
        m, n = call_stack.pop()
        if m == 0:
            yield _ackermann(call_stack, n + 1)
        elif n == 0:
            call_stack.append((m - 1, 1))
            yield _ackermann(call_stack, rv)
        else:
            # EEK
            yield _ackermann(call_stack, rv)


# ---

# The job of the recursive cases can be seen as breaking down complex inputs
# into simpler ones.
# NOTE: interesting idea on complexity

# - Algebraic data types
# - Inductively defined data (nats, linked list, bnf)

# ---

# [1]: http://www.artima.com/weblogs/viewpost.jsp?thread=98196
# [2]: http://paulbutler.org/archives/tail-recursion-in-python/
# [3]: http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html
# [4]: http://docs.python.org/2/library/sys.html#sys.setrecursionlimit
# [5]: http://www.cis.upenn.edu/~cis39903/static/10-rec-to-iter.pdf

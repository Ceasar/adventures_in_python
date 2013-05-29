"""
Shows the inconsistency of tuple initialization conventions.

This has existed since at least 1991.[1]

[1]: http://www.python.org/search/hypermail/python-1992/0278.html
"""


a = (1, 2,)

assert isinstance(a, tuple)

b = (1, 2)

assert isinstance(b, tuple)

c = (1,)

assert isinstance(c, tuple)

d = (1)

assert isinstance(d, int)

# e = (,)

# Invalid syntax

f = ()

assert isinstance(f, tuple)

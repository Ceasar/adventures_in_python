"""
Shows the inconsistency of some glyphs.

"""

# Tuple glyphs are inconsistent
#
# This has existed since at least 1991.[1]
# [1]: http://www.python.org/search/hypermail/python-1992/0278.html

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

# Set/dictionary glyphs are inconsistent

a, b = {1: 'a', 2: 'b'}, {1, 2}
c, d = {1: 'a'}, {1}
e, f = {}, {}

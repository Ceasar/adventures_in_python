"""
Behavior of tuple unpacking is fun.
"""

a, b = 1, 2

assert a == 1
assert b == 2

# Note it is actually assignment

o = [1, 2]

o[0], o[1] = 2, 1

assert o == [2, 1]

# This can be useful and strange

n = range(10)

n[5:] = range(5)

assert n == range(5) * 2

m = range(10)

m[0:10:2] = range(5)

assert m == [0, 1, 1, 3, 2, 5, 3, 7, 4, 9]

# things that are too long will override and append

aa = range(10)

aa[5:] = range(10)

assert aa == range(5) + range(10)

# we can also splice

ab = range(10)

ab[5:5] = range(10)

assert ab == range(5) + range(10) + range(5, 10)

# overwriting only happens in the designated range

ac = range(10)

ac[5:6] = range(10)

assert ac == range(5) + range(10) + range(6, 10)

# another way of effectively calling `list`

k = []

k[:] = 'abc'

assert k == ['a', 'b', 'c']

# Tuples can be unpacked structurally by mirroring form carefully

c, (d) = (1, (2,))

assert c == 1
assert d == (2,)

e, (f,) = (1, (2,))

assert e == 1
assert f == 2

u, [v] = [0, [1]]

assert u == 0
assert v == 1

s, t = 'ab'

assert s == 'a'
assert t == 'b'

# Note, Sets are sorted before unpacking

y, z = {1, 2}

assert y == 1
assert z == 2

w, x = {1, 0}

assert w == 0
assert x == 1

(r,) = (1,)

assert r == 1

# Note, this is a useful trick if you know a list only has one element

[q] = [1]

assert q == 1

# No luck with sets though

# {p} = {1}
# Can't assign to literal

# a curiosity

[] = []
[] = {}
[] = ()
[] = ''

# Names can be swapped through multiple assignment

g, h = 1, 2

g, h = h, g

assert g == 2
assert h == 1

# Names are assigned left to right

i, i = 1, 2

assert i == 2

j, k = k, j = 1, 2

assert j == 2
assert k == 1

# We can exploit this

k, k[:] = [], 'abc'

assert k == ['a', 'b', 'c']

# Functions can match tuples, but not anything else

def foo(a, (b, c), d):
    return a, b, c, d

assert foo(1, (2, 3), 4) == (1, 2, 3, 4)

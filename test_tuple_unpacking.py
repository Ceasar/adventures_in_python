"""
Behavior of tuple unpacking is fun.
"""

a, b = 1, 2

assert a == 1
assert b == 2

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

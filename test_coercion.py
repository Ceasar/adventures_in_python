# Coercion
# ========

# In ``x + y``, if *x* is a sequence that implements sequence concatenation,
# sequence concatenation is invoked.


xs = [1, 2, 3]

assert xs + xs == [1, 2, 3, 1, 2, 3]

ys = (1, 2, 3)

assert ys + ys == (1, 2, 3, 1, 2, 3)

zs = '123'

assert zs + zs == '123123'


# In ``x * y``, if one operator is a sequence that implements sequence
# repetition, and the other is an integer, sequence repetition is invoked.


assert xs * 2 == [1, 2, 3, 1, 2, 3]
assert ys * 2 == (1, 2, 3, 1, 2, 3)
assert zs * 2 == '123123'

# NOTE: The order of operands is irrelevant.

assert 2 * xs == xs * 2

# NOTE: Booleans are considered integers. Therefore, multiplication by booleans
# is permissible.

assert True == 1

assert xs * True == xs
assert xs * False == []

# Rich comparisons (implemented by method ``__eq__()`` and so on) never use
# coercion.

assert {} != []
assert bool({}) == bool([])


# Strings ints are converted to numbers

assert int('10') == 10

# String booleans are treated as regular strings

assert bool('False') == True


# backticks coerces things to repr
# (this is deprecated; use repr)

assert `[1, 2, 3]` == repr([1, 2, 3])

# Coercion
# ========

# In ``x + y``, if *x* is a sequence that implements sequence concatenation,
# sequence concatenation is invoked.

assert [1, 2, 3] + [1, 2, 3] == [1, 2, 3, 1, 2, 3]
assert (1, 2, 3) + (1, 2, 3) == (1, 2, 3, 1, 2, 3)
assert '123' + '123' == '123123'

# In ``x * y``, if one operator is a sequence that implements sequence
# repetition, and the other is an integer, sequence repetition is invoked.

assert [1, 2, 3] * 2 == [1, 2, 3, 1, 2, 3]
assert (1, 2, 3) * 2 == (1, 2, 3, 1, 2, 3)
assert '123' * 2 == '123123'

# NOTE: The order of operands is irrelevant.

assert 2 * [1, 2, 3] == [1, 2, 3] * 2

# NOTE: Booleans are considered integers. Therefore, multiplication by booleans
# is permissible.

assert True == 1
assert [1, 2, 3] * True == [1, 2, 3]

# Multiplying by 0 or False gives empty sequences

assert [1, 2, 3] * False == [1, 2, 3] * -1 == []

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


# __getitem__, typically used for implementing dict like indexing, is also used
# for iteration when __iter__ isn't present. The protocol specifies to
# repeatedly call __getitem__ with increasingly large values of ``n`` until an
# IndexError is raised. This suggests that 

class X():
    def __getitem__(self, n):
        if n < 10:
            return n
        raise IndexError()

assert list(X()) == range(10)

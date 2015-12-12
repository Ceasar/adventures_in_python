

A weird consequence of being able to chain comparisons (e.g. ``a < b < c`` or
``x < y > z`` is that you can write expressions like this::

    >>> False == False in [False]
    True

The Python docs clarify:

    Formally, if a, b, c, ..., y, z are expressions and op1, op2, ..., opN are
    comparison operators, then ``a op1 b op2 c ... y opN z`` is equivalent to
    ``a op1 b and b op2 c and ... y opN z``, except that each expression is
    evaluated at most once.

Weird thing on tuples::

    >>> a[0] += [1]
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    TypeError: 'tuple' object does not support item assignment
    >>> a
    ([1], [])

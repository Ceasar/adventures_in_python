
======
Glyphs
======

A glyph is an element of writing: an individual mark.

Python uses glyphs as a shorthand notation for common data structures::

    [1, 2] # list
    (1, 2) # tuple
    {1, 2} # set
    {'a': 1, 'b': 2} # dictionary

Bad Parts
---------

The syntax of tuple glyphs is inconsistent::

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

.. note::

    This has existed since at least 1991. See: http://www.python.org/search/hypermail/python-1992/0278.html

The glyphs for sets and dictionaries are potentially ambiguous::

    a, b = {1: 'a', 2: 'b'}, {1, 2}
    c, d = {1: 'a'}, {1}
    e, f = {}, {} # are these dictionaries or sets?

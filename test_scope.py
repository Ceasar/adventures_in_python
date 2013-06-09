from nose.tools import assert_raises


# *Names* refer to objects.

x = 1

# Names can refer to themselves.

l = []
l.append(l)
assert l == l[0]

# A *block* is a piece of Python program text that is executed as a unit.

# The following are blocks:
# - a module
# - a function body
# - a class defintion

# A code block is executed in an *execution frame*.

# A frame contains some administrative information (used for debugging) and
# determines where and how execution continues after the code block's execution
# has completed.


# A *scope* defines the visibility of a name within a block.

# If a local variable is defined in a block, its scope includes that block.

def test_block_scope():
    x = 1
    assert x == 1

# If the definition occurs in a function block, the scope extends to any blocks
# contained within the defining one, unless a contained block introduces a
# different binding for the name.


def test_function_scope():
    a = 42

    def foo():
        assert a == 42

    foo()

    def bar():
        a = 420
        assert a == 420

    bar()

# If a name is bound in a block, it is a local variable of that block.


def test_locals():
    x = 1
    assert 'x' in locals()

# If a name is bound at the module level, it is a global variable.

my_global = 1

assert 'my_global' in globals()

# Variables of a module are local and global.

assert 'my_global' in locals()

# If a name is not bound, but used, in a code block, it is a *free variable*.


def foo():  # global
    return x  # free variable

x = 0  # global

assert foo() == 0

# NOTE: There are only two scopes: globals and locals. This can sometimes lead
# to unintuitive, but predictable, behavior.


def bar(func):  # global
    x = 1  # local
    return func()

assert bar(foo) == 0


# The scope of names defined in a class block is limited to the class block;
# it does not extend to code blocks of methods


class BadMethodDefinition(object):
    a = 42

    def foo(self):
        assert a == 42


def test_bad_class():
    assert_raises(NameError, BadMethodDefinition().foo)


# This includes generator expressions since they are implemented using a
# function scope.


def bad_class_definition():
    class A:
        a = 42
        b = list(a + i for i in range(10))


def test_bad_class_definition():
    assert_raises(NameError, bad_class_definition)


# When a name is used in a code block, it is resolved using the nearest
# enclosing scope. The set of all such scopes visible to a code block is called
# the block's *environment*.

# When a name is not found at all, a ``NameError`` exception is raised.


def name_error():
    print bad_name


def test_name_error():
    assert_raises(NameError, name_error)


# If the name refers to a local variable that has not been bound, a
# ``UnboundLocalError`` exception is raised.


def unbound_local_0():
    x = x + 2


def test_unbound_local_0():
    assert_raises(UnboundLocalError, unbound_local_0)

# NOTE: This can sometimes lead to strange behavior


def bound_local_0():
    a = 42
    b = 42

    def foo():
        assert a == 42
        b = 43
        assert b == 43

    foo()
    assert a == 42
    assert b == 42

bound_local_0()


def unbound_local_1():
    a = 42
    b = 42

    def foo():
        assert a == 42
        assert b == 42

        b = 43
        assert b == 43

    foo()
    assert a == 42
    assert b == 42


def test_unbound_local_1():
    assert_raises(UnboundLocalError, unbound_local_1)

# The following constructs bind names:

# - formal parameters to functions


def foo(x):
    assert x

foo(1)

# - import statements

import os

assert os

# - class and function definitions


def special_foo():
    pass

assert special_foo

# - assignment

z = 1

assert z

# - `for` loop header

for y in range(10):
    pass

assert y

# NOTE: this also includes list comprehensions

q = [u for u in range(10)]

assert u

# - except clause header

try:
    raise Exception()
except Exception as e:
    pass

assert e

# - with statement

with open('/dev/null', 'w') as f:
    pass

assert f

# The ``import`` statement of the form ``from ... import *`` binds all names
# defined in the imported module, except those beginning with an underscore.
# The form may only be used at the module level.


def warning():
    # from os import *
    # SyntaxWarning: import * only allowed at module level
    pass


# del x
# name 'x' is not defined

# A clever mess with names and references, from Guido himself:
# http://neopythonic.blogspot.com/2009/04/tail-recursion-elimination.html


def f(x):
    if x > 0:
        return f(x-1)
    return 0

g = f


def f(x):
    return x

assert g(5) == 4

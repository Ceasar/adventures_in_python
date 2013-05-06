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

# If the definition occurs in a function block, the scope extends to any blocks
# contained within the defining one, unless a contained block introduces a
# different binding for the name.


def test_good_scope():
    a = 42

    def foo():
        assert a == 42

        def bar():
            assert a == 42

        bar()
    foo()


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


def unbound_local_error():
    x = x + 2


def test_unbound_local_error():
    assert_raises(UnboundLocalError, unbound_local_error)


# The ``import`` statement of the form ``from ... import *`` binds all names
# defined in the imported module, except those beginning with an underscore.
# The form may only be used at the module level.


def test():
    # from os import *
    # SyntaxWarning: import * only allowed at module level
    pass


# del x
# name 'x' is not defined

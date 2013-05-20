"""
Adventures in inheritance.
"""

#  Demonstrate the strange interaction between hidden methods and subclassing.


class Foo(object):
    def __do_something(self):
        return "Foo"

    def trigger(self):
        return self.__do_something()

assert Foo().trigger() == "Foo"


class Bar(Foo):
    def __do_something(self):
        return "Bar"

assert Bar().trigger() == "Foo"


class FooBar(Foo):
    def __do_something(self):
        return "FooBar"

    def trigger(self):
        return self.__do_something()


assert FooBar().trigger() == "FooBar"


class BarFoo(Foo):
    def trigger(self):
        return self.__do_something()

# This raises an error
# assert BarFoo().trigger() == "Foo"

# We might say then, that 'Class.method' is public, 'Class._method' is
# protected, and 'Class.__method' is private.

# Method Resolution Order


class Maybe():
    def trigger(self):
        return "Main"


class Left(Maybe):
    def trigger(self):
        return "Left"


class Right(Maybe):
    def trigger(self):
        return "Right"


# Classes that inherit from multiple classes that define the same name use
# the name defined on the left most inherited class.

class LeftRight(Left, Right):
    pass

assert LeftRight().trigger() == "Left"


class RightLeft(Right, Left):
    pass

assert RightLeft().trigger() == "Right"


# Repeated Inheritance still follows the regular MRO.

class RightLeftLeft(RightLeft, Left):
    pass

assert RightLeftLeft().trigger() == "Right"


class LeftLeft(Left, Left):
    pass

assert LeftLeft().trigger() == "Left"

# TODO: Adventures with super!

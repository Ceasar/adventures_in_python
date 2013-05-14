"""
Demonstrate the strange interaction between hidden methods and subclassing.
"""
 
 
class Foo(object):
    def __do_something(self):
        print "Foo is doing something"
 
    def trigger(self):
        self.__do_something()
 
 
class Bar(Foo):
    def __do_something(self):
        print "Bar is doing something"
 
 
class FooBar(Foo):
    def __do_something(self):
        print "FooBar is doing something"
 
    def trigger(self):
        self.__do_something()
 
 
 
Foo().trigger() # Prints "Foo is doing something"
Bar().trigger() # Prints "Foo is doing something"
FooBar().trigger() # Prints "FooBar is doing something"

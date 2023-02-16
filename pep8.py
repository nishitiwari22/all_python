# Style Guide of Python


def long_function_name_with_long_args(
    argument1,
    argument2,
    argument3,
    argumnet4,
    argument5,
    argument6,
    argument7,
    argument8,
):
    print("run")


# 4 Spaces for all Indentation
# Python uses snake case.

# hello_world (This is Snake case)
# helloWorld (This is Camel Case)
# HelloWorld (This is Pascal Case)


# Naming Conventions for constant
# BG_COLOR = (255, 255, 255)

# Naming Conventions for funcions
# def hello_world() (This is correct)

# def helloWorld() (This is incorrect)

# Naming Conventions for Class
# class BaseClass:

# class BaseException (This is built-in in Python. And exception is a class in python. )

# Method Parameter Naming


class Test:
    def test(self):
        pass


# By convention the first paramter should be named self. However I can name it anything.


@classmethod
def cls_method(cls):
    pass


# By convention the first paramter should be named cls.

# Functions and classes have two lines between them if they are in the top level. If they are nested inside one space will do fine. Methods inside class we seperate them with one line.


# Importing somethng from a module. You can import on the same line.
# example: from os import path, stat

# Avoid wild card.
# example: from os import * (This doesn't clearly states what toy want to import from OS)

# "HELLO'"
# 'hello"'
# Both are correct

# Doc string(Always use double quotation marks)

# Whitspaces

# # Correct

# COLOR = (0, 255, 0)  # This is correct

# COLOR = (0, 255, 0) #this is incorrect (1st letter must be capital)


# Try and Except

# Correct

try:
    import platform_specific_module
except ImportError:
    platform_specific_module = None

# Wrong


try:
    import platform_specific_module
except:
    platform_specific_module = None
    # Don't do an empty expect block

    # Correct
if foo.startswith("bar"):
    pass
    # Wrong
if foo[:3] == "bar":
    pass

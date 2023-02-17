#  This stuff is going to be advance:

#  https://www.youtube.com/watch?v=ScUKeVuL7Y8

# Pretty much everything is an object in Python

# x = 1
# X is an instance of class int
# print(type(x))
#  These classes are like the blueprints that define the behavior of different objects in Python

y = "str"
print(type(y))

# print(x + y)
#  This will give error


class Person:
    def __int__(self, name):
        self.name("name")


self = "nishi"

print(type(Person))

#  There is a blueprint of how classes are created.


# def foo(x):
#     print(x)


# print(type(foo))

# #  There is a blueprint that defines function.

# *******   Advance behavior of Classes*******
# Classes are of type type. This means that I can create subclass of class type and use that class to create new classes

def person_init(self, name, age):
    self.name = name
    self.age = age



def say_name(self):
    print(self.name)


new_class = type("Person", (), {"__init__": person_init, "say_name": say_name})
print(new_class.__name__)
x = new_class("Nishi")
print(x.name)

#  Three argument that goes here are class name. And anything that will inherit will go in round brackets also known as base class. And attributes will go in curly brackets like class methods, class variables.

# This can allow to create a new class


# Use Cases and Metaclass Introduction

class CreateClass(type):
    
    #  Creating a class that inherits from type and now I can change the behavior of type. And so I change how class are created
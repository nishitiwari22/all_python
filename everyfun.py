# #******Absolute Value*******
# #abs()

# class ImplementAbs:
#     def __init__(self, string):
#         self.string = string

#         def __abs__(self):
#             return self.string.lower()

# # custom_obj = ImplementAbs("HELLO")

# x = abs(-9)
# y = abs(-100.876)
# # z = abs(custom_obj)

# print(x)
# print(y)
# # print(z) (This should print HELLO in lowercase but it is not find why?)


# *******Asynchronous Iterator (This is little advanced topic)********
#  aiter()
# import asyncio
# import string

# class AsyncIterator:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop

#     def __aiter__(self):
#         self.cur = self.start
#         return self

#     async def __anext__(self):
#         await asyncio.sleep(1)
#         if self.cur >= self.stop:
#             raise StopAsyncIteration

#         self.cur +=1
#         return self.cur - 1


# async def example():
#     custom_obj = AsyncIterator(1,10)
#     obj_iter = aiter(custom_obj)
#     print(obj_iter)
#     async for num in obj_iter:
#         print(num)

# asyncio.run(example())


# #*****All********
# #all()

# a = [1,0,1,2,3]
# print(all(a))
# #  Zero is a falsy value

# b = [True, True, 1, 2]
# print(all(b))

# c = ["", "a", "b"]
# print(all(c))
# #  Empty string is a falsy value

# d = [[0,0], [0,0], [0,0]]
# print(all(d))
# #  Falsy value but list contains elements so it becomes a truthy value


# e = [[], [1], [True]]
# print(all(e))
# #  Empty list is a falsy value


# *******Asynchronous Iterator (This is little advanced topic)*********
# anext()
# import asyncio


# class AsyncIterator:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop

#     def __aiter__(self):
#         self.cur = self.start
#         return self

#     async def __anext__(self):
#         await asyncio.sleep(1)
#         if self.cur >= self.stop:
#             raise StopAsyncIteration

#         self.cur +=1
#         return self.cur - 1


# async def example():
#     custom_obj = AsyncIterator(1,10)
#     obj_iter = aiter(custom_obj)
#     print(await anext(obj_iter))
#     print(await anext(obj_iter))
#     print(await anext(obj_iter))

# asyncio.run(example())


# # #*****Any********
# #any()

# a = [1,0,1,2,3]
# print(any(a))

# b = [True, True, 1, 2]
# print(any(b))

# c = ["", "a", "b"]
# print(any(c))

# d = [[0,0], [0,0], [0,0]]
# print(any(d))


# e = [[], False, 0]
# print(any(e))
# #  All are falsy value


# #****Binary********
# bin()

# base10 = 100
# base2 = bin(base10)

# base10_neg = -100
# base2_neg = bin(base10_neg)
# ##Ismai 2's compleent ki jagah humko yeh negative mai deta hai  format() method bhi use kar sakte hai hum alag type se

# print(base2)
# print(base2_neg)


# ***** #Boolean ********
# #bool()
# # The only falsy integer value is zero
# print(bool)
# print(bool(""))
# print(bool(1))
# print(bool(-1))
# print(bool([1,2]))
# print(bool({}))
# print(bool({"key": "value"}))


# #Callable
# #callable()

# from ast import Lambda

# class Class:
#     pass

# def func():
#     print("h1")

# def func2():
#     def inner():
#         pass

#     return inner

# # func3 = Lambda x: x + 1 (ye wala ram jaane kyu error de raha hai)
# not_func = "hello"

# print(callable(Class))
# print(callable(func))
# print(callable(func2()))
# # print(callable(func3))
# print(callable(not_func))


# #Character
# #chr()

# A = 65
# a = 97

# print(chr(A))
# print(chr(a))

# # Useful when user wants to generate a sequence of characters and user don't have to type a bunch of them out

# Class Method
# classmethod()


# class TestClass:
#     def regular_method(self):
#         print(self)

#     @classmethod
#     def class_method(cls):
#         print(cls)

#     def __str__(self):
#         return "TestClass Instance"


# t = TestClass()
# t.regular_method()
# t.class_method()
# TestClass.class_method()


# Complex Number
# complex()

# complex1 = "32+2j"
# print(complex(complex1))

# print(complex(3, 4))

# Complex numbers aren't only used in Physics. They're a mathimatical concept, a complex number describes a point on a plane using 2 coordinates and uses the imaginary number i with i² = -1, as the second axis, so you can write any complex number in the form a + bi with a and b being Real Numbers. Python uses j instead of i to not confuse people with the common name for iteration variables.

# Complex Numbers are also used in Physics but atleast in my experience you'll be using Vectors (which is another math concept of Numbers on a n-Dimensional Plane) more often than Complex numbers.

# Delete Attribute
# delattr()


# class MyClass:
#     def __init__(self, x):
#         self.x = x


# c = MyClass(10)

# print(c.x)
# delattr(c, "x")
# print(c.x)


# Dictionary
# dict()

# lst = [("a", 1), ("b", 2)]
# lst_dict = dict(lst)

# print(lst_dict)

# Directory?
# dir()

# import math
# print(dir(dict))

# Division Modulo/Modulus
# divmod()
# from math import remainder


# quotient, remainder = divmod(10, 3)
# print(quotient, remainder)


# Enumerate
# enumerate()

# values = [(0, 'a'), (1, 'b'), (2, 'c'), (3 'd')]
# for index, value in values:
#     print(f"{index}: {values}")

# print(list(enumerate(values)))

#  Evaluate # Eval can be pretty dangerous
# eval()

# x = 2
# code = input("Enter some code: ")
# eval(code)

# execution
# exec()

# code = input("Enter some code: ")
# exec(code)

# x = 0; x+= 1; print(x); (It will give output 1) (It can also change the value of variables)

# Filter
# filter()


# def filter_func(value):
#     return value % 2 == 0


# lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# evens = filter(lambda x: x % 2 == 0, lst)
# evens_2 = filter(filter_func, lst)

# print(evens)
# print(evens_2)

# print(list(evens))
# print(list(evens_2))


# Float
# float()

# x = 1
# x_float = float(1)

# string = "9.8"
# string_float = float(string)

# print(float("inf"))
# print(float("-inf"))
# print(float("1e-003"))


# Format
#  # format()

# from logging.config import valid_ident


# txt = "For only {price: .2f} dollars!"
# print(txt.format(price=49))

# binary_value = format(100, "b")
# print(binary_value)

# [[fill] align][sign][#][0][width][, [.precision][type]
# where, the options are
# fill ::= any character
# align ::= "<" | ">" | "=" | "^"
# sign ::= "+" | "-" | " "
# width ::: integer
# precision ::= integer
# type ::= "b" I "c" | "d" | "e" | "E" | "F" | "F" | "g" | "G" |


# Frozen Set
# frozenset()

# Can be used as keys in dictionaries

# lst = [1, 2, 3]
# s = set(lst)
# s.add(4)

# print(s)

# fs = frozenset(lst)
# print(fs)


# Get Attribute
# getattr


# class MyClass:
#     def __init__(self, x):
#         self.x = x


# c = MyClass(10)
# print(getattr(c, "x"))


# Has Attribute
# hasattr()


# class MyClass:
#     def __init__(self, x):
#         self.x = x


# c = MyClass(10)
# print(hasattr(c, "x"))
# print(hasattr(c, "y"))


# Help
# help()

# help(int)  # gives documentation


# Hexadecimal
# hex()


# class CustomHex:
#     def __index__(self):  # Only works for a class who implements underscore underscore method
#         return 10


# print(hex(255))
# print(hex(1))

# c = CustomHex()
# print(hex(c))


# Id (To check if two objects are same or not. It will create alias)
# id()

# x = [1, 2, 3]
# y = x
# a = 100000
# b = a + 1 - 1

# print(id(x))
# print(id(y))
# print()
# print(id(a))
# print(id(b))


# Input   # Input is always entered as a string
#  input()

# inp = input("I know what this does:")


#  Integer
#  int()

# print(int(True))
# print(int(False))
# print(int("123"))
# print(int("-123"))
# print(int(9.7))
# print(int("0b11001", base=2))


#  Is Instance
# isinstance()

# a = 1
# b = 2

# print(isinstance(a, int))
# print(isinstance(b, float))
# print(isinstance(a, type))
# print(isinstance(int, type))  # int is of type type because all of our classes are type type.


#  Is Subclass
# issubclass()


# class A:
#     pass


# class B:
#     pass


# class C(A):
#     pass


# class D(C):
#     pass


# class E(A, B):
#     pass


# print(issubclass(C, A))
# print(issubclass(D, C))
# print(issubclass(D, A))
# print(issubclass(E, A))
# print(issubclass(E, B))


# Iterator
# iter()


class Iterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop

    def __iter__(self):
        self.cur = self.start
        return self

    def __next__(self):
        if self.cur >= self.stop:
            raise StopIteration

        self.cur += 1
        return self.cur - 1


def example():
    custom_obj = Iterator(1, 10)
    obj_iter = iter(custom_obj)
    print(obj_iter)
    for num in obj_iter:
        print(num)


example()

#  ****************** Part 2****************    H - Z

# quit() python function

#  It's not there because exit() and quit() are from site-module which is allways called without import.
# You really should not use these functions in code, they only exist to help beginers to get out of python prompt.
#  One should use instead:
#  sys.exit()
# or just purely:
# raise SystemExit (in the end all of these just raises this exception)


# Hash
# has()

# key = "randomstring"
# print(hash(key))

# num_hash = hash((1, 2))
# print(num_hash)


# Length
# len()


# class Custom:
#     def __len__(self):
#         return 5


# c = Custom()
# print(len(c))

# x = [1, 2, 3, 4, 5]
# print(len(x))

# y = "string"
# print(len(y))

# items = {1: 1, 2: 2, 3: 3}
# print(len(items))

# s = set([1, 2, 3])
# print(len(s))


# Locals
# locals()

# print(locals())
# (locals()["__file__"])
# print(__file__)


# Map
# Map()

# vals = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# squares = map(lambda x: x**2, vals)
# print(list(squares))

# items = {"A": 1, "B": 3, "C": 4}
# strings = map(lambda key: items[key] * key, items)
# print(list(strings))


# Maximum
# max()

# numbers = [0, -9, 8, 6, 0, 2, 34]
# print(max(numbers))

# print(max(3, 4, 5, 9, -1))

# print(
#     max("hello", "world", "yes", "ya")
# )  #  Ismai ASCII value ke basis par judge kiya jata hai

# print(
#     max([1, 2, 3, 4], [1, 2, 4], [2, 1])
# )  # Ismai list mai jo starting number max hai wo print hoga


# class Custom:
#     def __init(self, val):
#         self.val = val


# c1 = Custom(1)
# c2 = Custom(2)
# c3 = Custom(3)

# print(max(c1, c2, c3, key=lambda x: x.val))  # ye nhi samjha


# Minimum
# mix()

# numbers = [0, -9, 8, 6, 0, 2, 34]
# print(min(numbers))

# print(min(3, 4, 5, 9, -1))

# print(
#     min("hello", "world", "yes", "ya")
# )  #  Ismai ASCII value ke basis par judge kiya jata hai

# print(
#     min([1, 2, 3, 4], [1, 2, 4], [2, 1])
# )  # Ismai list mai jo starting number minimum hai wo print hoga


# class Custom:
#     def __init(self, val):
#         self.val = val


# c1 = Custom(1)
# c2 = Custom(2)
# c3 = Custom(3)

# print(min(c1, c2, c3, key=lambda x: x.val))  # ye nhi samjha

# Memory View
# memoryview()

# x = b"abcdef"
# mem = memoryview(x)

# print(mem[1])
# print(chr(mem[1]))

# print(mem[1:4])
# print(bytes(mem[1:4]))


# Next
# next()


# class Iterator:
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop

#     def ___iter__(self):
#         self.cur = self.sstart
#         return self

#     def __next__(self):
#         if self.cur >= self.stop:
#             raise StopIteration

#         self.cur += 1
#         return self.cur - 1


# custom_obj = Iterator(1, 10)
# obj_iter = iter(custom_obj)
# print(next(obj_iter))
# print(next(obj_iter))
# print(next(obj_iter))


#  Output TypeError: 'Iterator' object is not iterable

# Object
# object()

# empty = object()
# print(empty)
# print(dir(empty))


# Octal
# oct()

# print(oct(10))
# print(oct(100))
# print(oct(-98))


# Open
# open()


# Power
# pow()

# x = pow(10, 2)  # -> 100
# print(x)

# y = pow(10, -2)  # -> 0.01
# print(y)

# pow_with_mod = pow(11, 3, 6)
# print(pow_with_mod)
# 11 ^ 3 = 1331
# 1331 % 6 == 5

# Print
# print()

# print("hello", "world")
# print("hello", "world", sep="|")
# print("hello", end="|END|")
# print("okay?")


# Property
# property()


# Range
# range()

# r1 = range(1, 10)  # Last value is excluded.
# print(list(r1))

# r2 = range(1, 10, 2) # It's means take 2 steps.
# print(list(r2))

# r3 = range(10)
# print(list(r3))

# r4 = range(-1, -10, -2)
# print(list(r4))


# Representation
# repr()


# class Pet:
#     def __init__(self, name):
#         self.name = name

#     def __repr__(self):
#         return f"Pet(name={self.name})"


# p = Pet("Billy")
# p2 = Pet("Sally")

# print(repr(p))
# print(repr(p2))


# Reversed
# reversed()

# lst = [1, 2, 3]
# lst_reversed = reversed(lst)
# print(list(lst_reversed))

# tup = (1, 2, 3)
# tup_reversed = reversed(tup)
# print(tuple(tup_reversed))

# string = "hello"
# string_reversed = reversed(string)
# print(list(string_reversed))


# Round
# round()

# x = 10.5
# print(round(x))

# y = 10.234232
# print(round(y, 4))  # Point ke baad 4 number print karega

# z = 0.828
# print(round(z, 10))


# Set
# set()

# lst = [1, 1, 2, 2, 3, 3, 3, 4]
# lst_set = set(lst)
# print(lst_set)

# s = {6, 6, 7 * lst}
# print(s)

# new_set = set()
# print(type(new_set))

# new_dict = {}
# print(type(new_dict))


# Slice
# slice()

# lst = [2, 4, 6, 8, 10]
# s = slice(1, 3)
# print(lst[s])

# lst = [2, 4, 6, 8, 10]
# s = slice(1, 5, 2)
# print(lst[s])


# Sorted
# sorted()

# Static Method
# @staticmethod [This is a decorator]


# class Helpers:
#     @staticmethod
#     def add(x, y):
#         return x + y


# _sum = Helpers.add(1, 2)
# print(_sum)

# h = Helpers()
# _sum2 = h.add(1, 2)
# print(_sum2)


# String
# str()

# Sum
# sum()

# lst = [4, 5, 2, 4.3, 5, 7, 9, 10, -9]
# print(sum(lst))

# start_sum = sum(lst, start=5)  # adds 5 to sum
# print(start_sum)

# s = {1, 4, 5, 3, 2, 1}
# print(sum(s))


# Tuple
# tuple()

# pairs = [[1, 2], [3, 4], [5, 6]]
# tuples = tuple(pairs)
# print(tuples)

# string = "hsjdgj"
# str_tuple = tuple(string)
# print(str_tuple)


# Type
# type()

# x = 1
# print(type(x))


# def func():
#     pass


# print(type(func))

# ClassName = type(
#     "ClassName",
#     (object,),
#     {
#         {"attribute": "i am an attribute", "add1": lambda self, x: x + 1},
#     },
# )

# c = ClassName()
# print(c.attribute)
# print(c.add1(2))


# Variables  # Duniya bhar ka variables print kar diya
# vars()

# print(vars())

# print(vars(list))


# class Custom:
#     test_var = "hello"


# print(vars(Custom))


# Zip
# zip()

# widths = [4, 5, 6, 7, 2, 1]
# heights = [5, 3, 1, 2, 3, 1]
# zipped = zip(widths, heights)
# print(zipped)
# print(list(zipped))

# string = "hello"
# values = [1, 2, 3]
# zipped2 = zip(string, values)
# print(list(zipped2))


# property
# repr
# open
# set
# sorted
# static mentod(learn)
# STRING
# super

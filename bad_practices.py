# ************* Mutable Default Parameter***************


# def append_number(num, numbers=[]):
#     numbers.append(num)
#     print(num)
#     print(numbers)
#     return numbers


# x = append_number(1)
# y = append_number(2)
# print(x is y) # If the objects are same the 'is' keyword return true.

#  We are modifying same object in different function and so the second output gives [1,2] which means in same list 2 is getting append.

# def append_string(s, string="hello"):
#     string += s
#     print(s)
#     print(string)
#     return string

# append_string("h")
# append_string("i")

#  String is a non-mutable data type so instead of getting changed in the same it creates a brand new string

#  Don't use a mutable default parameter in this case because of the some results


# ********************* Not using a default Dict*******************

# counts = {}
# numbers = [1, 2, 3, 4, 2, 3, 4, 1, 5]
# for key in numbers:
#     if key not in counts:
#         counts[key] = 0
#     counts[key] += 1

# from collections import defaultdict
# from logging.config import valid_ident


# # def func():
# #     return 0


# count = defaultdict(lambda: 0)
# numbers = [1, 2, 3, 4, 2, 3, 4, 1, 5]
# for key in numbers:
#     counts[key] += 1

# print(counts)

# Using a default dict in the mentioned case is not really pythonic either, since there is a counter in the collections module. The code would then become:

# from collections import Counter
# numbers = [ ... ]
# c = Counter(numbers)

# the Counter API offers a lot of additional functionality and is generally to be preferred over the default dict. The default dict should be used when there is some additional work to do on insertion, like it was done in the second case.


# Regarding the context manager: If you catch yourself writing many try–finally blocks, that is normally the moment to use one. You can also implement custom managers for your own classes via the dunder methods `__enter__` and `__exit__`. Those are what is executed by the with statement:

# with Foo(args) as bar:
#     baz()

# more or less de sugars to

# bar = Foo.__enter__(args)
# try:
#     baz()
# finally:
#     Foo.__exit__()


# `defaultdict(lambda: 0)` should be replaced with `defaultdict(int)` imo

# also id, zip, and list are not built-in keywords, rather they're built-in functions


#  ********************Not using context manager when opening files****************.
# f = open("file.txt", "w")
# f.write("hello")
# f.close()

#  Above is not a pythonic way to do it and can cause errors better to use the below one.

# with open("file.txt", "w") as f:
#     f.write("hello")


#  *********Not using Enumerate******** (Prints indexes and items)

# lst = [1, 2, 3, 4, 5, 6, 7, 8]

# for i in range(len(lst)):
#     val = lst[i]
#     print(val)

#  Above is not that better way to do it better to use the below one.

# for i, val in enumerate(lst):
#     print(i, val)

#  It will work for any iterable object like strings and set as well.


# d = {"hello": 1, "name": 2}

# for i, val in enumerate(d):
#     print(i, val)


# **********Overriding Built-In Names

# id = 2   # We will be unable to use the id as 'id' keyword in Python better not to use Python keywords or if it is important to use the exact same work add underscores
# id_ = 3 # Correct way
# _id = 4 # Correct way (It will make the attribute private)
# zip = 90001
# list = []

# print(id)
# x = 2
# id(x)

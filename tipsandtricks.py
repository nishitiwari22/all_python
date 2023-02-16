# *****Enum Class*****


# class Enum:
#     Nishi, Sabika, Aafreen = range(1, 4)


# print(Enum.Nishi == 1)

# ******Multiline Assignment*****

# x, y, z = 1, 4, 7
# x, y, z = [1, 4, 7]
# x, y, z = (1, 4, 7)
# print(y)
# print(z)

#  *****Fstrings*******

# name = "Nishi"
# age = 15
# print("Hello my name is", name, "and I am", age, "years old")
# print("Hello my name is" + name + "and I am " + str(age) + " years old")

# st = f"Hello my name is {name} and I am {age} years old"

# st = f"Hello my name is {name} and I am {age} years old"

# st = f"Hello my name is {name} and I am {age + 5} years old"
# print(st)
# st = f"Hello my name is {name} and I am {age + 5} years old"
# print(st)

# *****List enumeration*******

# x = [3, 5, 7]

# for i in range(len(x)):
#     print(i, x[i])

# Enumerate functions allow us to access the index and the element at the same time. Pairs every element in the list with the corresponding index

# a = [6, 7, 8, 9]

# for i, e in enumerate(a):
#     print(i, e)


#  Zip Function

# name = ["Nishi", "Aarushi", "Ritu"]
# age = [20, 19, 21]
# fav_color = ["Orange", "Pink", "Yellow"]

# print(list(zip(name, age, fav_color)))

#  Iterating Zip

# for tup in zip(name, age, fav_color):
#     print(tup)

# for i in range(len(name)):
#     print(name[i], age[i], fav_color[i])


# help(list)

import os

help(os)

# ****** This ********
# import this
## outputs a poem


## ******** Antigravity*******
# import antigravity
# opens comic in browser

# ******* walrus operator******

# def func(x):
#     # do some long computation
#     return x + 1

# := func(2)
# := is a walrus operator
# This will give an error because it is not under parentheses or under if or any loop statemnets.
# if func(4) >= 5:
#     print(func(4))
# The above thing is ineffective because I am calling the function twice instead use the walrus operator

# (x := func(2))
# print(x)

# if x := func(4) >= 5:
#     print(x)
# We get the ouput as True whihc is actually strange. The reason is we assigned 'x' equal to the above expression. The precedence of walrus operator comes after the greater than equal to operator that's why we are getting the value true.


# # ****Some random info*****
#     # is !=  ==
# d, e = [], []
# print( d == e)
# # Empty list is equivalent to empty list. Therefore the ouptut is 'True'
# print(d is e)
# # This will give the output 'False' because they are not the exact same empty list. Because both empty lists are stored in different memory location. Basically the above print statement is doing this.
# print(id(d) == id(e))


a = "".join(["o", "k", "a", "y"])
# .Join method is run at run time and not at compile time.

b = "o" + "k" + "a" + "y"

c = "okay"

print(a, b, c)

print(a is b)
print(a is c)
print(b is c)

# Strings are imuutable data types in Python. When we create an immutable object it creates a new memory in object.

# This is happening because of 'INTERN'. Now 'INTERNING' is a method of storing only one copy of each distinct string value, whihc must be immutable.


## ***** Chained Operations****

print((1 == 1) in [1])
print(1 == (1 in [1]))
print(1 < (0 < 1))
print(1 < 0 < 1)



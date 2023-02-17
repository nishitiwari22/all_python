import sys

# x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# y = map(lambda i: i**2, x)
# print(y)
# print(
#     list(y)
# )  #  It's not storing this list it is creating this list for us when we call the list function.

# for i in y:
#     print(i)

# print(
#     sys.getsizeof(list(y))
# )  # How come the output is 184 in my laptop and in Tim's computer 152
# print(sys.getsizeof(y))  # And 48 is common in my and tim's computer but how 48


# An iterator is that allows us to loop through a sequence of numbers or have some data without having to store them of
# Example: Range
# next()
#  Next value in the iteration through an iterator

# print(next(y))
# print(next(y))
# print(next(y))
# print(next(y))

# print(y.__next__())

#  Above is a dunder method a double underscore method

# print("For Loop Stars")
# for i in y:
#     print(i)
# #  In this case the above for loop and the below while loop are exactly the same thing.

# while True:
#     try:
#         value = next(y)
#         print(value)
#     except StopIteration:
#         print("Done")
#     break


# x = range(1, 11)
# print(x)

# iter()

# It returns an iterator from an object

# next(x) #  This gives error range object is not an iterator
# print(next(iter(x)))

# for i in iter(x)  #  It calls the iter method gets the iterator and then calls the next method on the iterator object that we got from the object we're looping through.


# Creating Legacy Iterators

#  Old School way of creating an iter
# class Iter:
#     def __init__(self, n):
#         self.n = n

#     def __iter__(self):
#         self.current = -1
#         return self

#     #  If I remove the above function I'll get an error of 'Iter' object is not iterable.

#     def __next__(self):
#         self.current += 1

#         if self.current >= self.n:
#             raise StopIteration

#         return self.current


# x = Iter(5)

# # for i in x:
# #     print(i)

# itr = iter(x)
# # print(next(x))  #  If I only write this it gives error 'Iter' object has no attribute 'current'
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(next(itr))


#  Creating Generators


# def gen(n):
#     for i in range(n):
#         yield i


# Exactly same as the class we just created
# When the yield keyword is hit, it pauses the execution of function and returns this value to whatever is iterating through this generator object.
# IMP thing:  When yield is hit, the function execution is paused it's not terminated.
# for i in gen(5):
#     print(i)


# def gen():
#     yield 1
#     print("Pause 1")
#     yield 2
#     print("Pause 2")
#     yield 3
#     print("Pause 3")
#     yield 4


# x = gen()
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))


#  Generators Use Case

#  Loop through a sequence or some large amount of data without needing to store all of it. You don't care about the data which will come before or after iteration, you only care about the current piece of data.
# Example: Printing all the numbers in the sequence and in case you need the access of before or after element you can't use the generator.


# def csv_reader(file_name):
#     for row in open(file_name, "r"):
#         yield row


#  Generator Comprehensions

#  Way of creating a generator that not involves a function

x = (i for i in range(10))  #  My stupid generator

for j in x:
    print(j)


# A great coding exercise would be, print inorder traversal of binary tree using generators.


#  Assuming this is the tree you wanted:
# 	    	A
# 	     /       \
# 	 B		C
#        /  \            /    \
#     D	    E       F     G

# The result = (D, B, E, A, F, C, G)

# From what I can gather, generators can be used to calculate the next part of the result only when it's needed, instead of searching the entire tree which may take a long time.
# Say you only wanted to traverse the left half of the tree, using generators you can start traversing the tree and keep fetching the next result until you find the root node.
# For the tree above this would be (D, B, E, A).
# By doing this it has allowed us to get the parts we need without searching the entire tree therefore it has saved us time.
# It also allows us to make use of the generator benefits that Tim explained such as less memory usage as it's not storing the entire search result, its only storing what is currently being used.


#  the benefit of using a generator is that the function is only a few lines long:
# def traverse(tree):
#   if tree is None:
#     return
#   yield from traverse(tree.left)
#   yield tree.value
#   yield from traverse(tree.right)

# for el in traverse(my_tree):
#   print(el)

# For comparison, to do this iteratively, you need to keep a stack of the parent nodes you've visited, and to do this recursively, you need a helper function that keeps track of how many elements you've seen.

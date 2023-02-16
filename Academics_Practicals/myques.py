

# **** Explain list and it's methods****

fruits = ["Orange", "Apple", "Pear", "Grape"]
print(fruits)

# List is a comma separated item enclosed in square bracket and is mutable.
# Tuple is a comma separated item enclosed in round braces and is immutable.
# Set uses set keyword  with comma-separated items enclosed with both square and round braces and can also be created in curly braces. It is unordered collection with no duplicate elements

fruits[0] = "Pear"
print(fruits)

# animals = ("Lion", "Zebra", "Deer")
# print(animals)
# animals[0] = "Crocodile"
# print(animals)

# names = set(["Nishi", "Sabika", "Ritu"])
# print(names)
# type(names)


# Methods in List

# 1	append() Used for appending and adding elements to the end of the List.
# fruits.append("Strawberry")
# print(fruits)

# # 2	copy()	It returns a shallow copy of a list. It takes no arguments
# fruits.copy()
# print(fruits)

# 3	clear()	This method is used for removing all items from the list.
# fruits.clear()
# print(fruits)

# 4	count()	This methods count the elements. Calculates total occurrence of a given element of List.
# print(fruits.count("Pear"))

# 5	extend() Adds each element of the iterable to the end of the List
# print(fruits.extend("Berries"))

# 6	index()	Returns the lowest index where the element appears.
# print(fruits.index("Pear"))

# # 7	insert() Inserts a given element at a given index in a list.
# fruits.insert(2, "Berry")
# print(fruits)

# # 8	pop() Removes and returns the last value from the List or the given index value.
# fruits.pop(2)
# print(fruits)

# # 9	remove() Removes a given object from the List.
# fruits.remove("Apple")
# print(fruits)

# # 10 reverse() Reverses objects of the List in place.
# fruits.reverse()
# print(fruits)
# # 11 sort() Sort a List in ascending, descending, or user-defined order
# fruits.sort()
# print(fruits)


# **** Explain string and it's methods****

# A string is any series of characters that are interpreted literally by a script
#  All string methods returns new values. They do not change the original string.



# **** Explain loop****

# A loop is a sequence of instructions that is continually repeated until a certain condition is reached.
# Types:
# while loop
# for loop
# nested loop

# **** Explain conditional statement****


# Conditional statements are also known as decision-making statements. We need to use these conditional statements to execute the specific block of code to check if the given condition is true or false.

# In Python we can achieve decision making by using the following statements:

# if statements
# if-else statements
# elif statements
# Nested if and if-else statements
# elif ladder


# **** Explain File-handling****

# Python treats files differently as text or binary and this is important. Each line of code includes a sequence of characters and they form a text file. Each line of a file is terminated with a special character, called the EOL or End of Line characters like comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun.

# f= open("C:\\Users\\great\\Desktop\\Nishi\\Coding\\Python\N.txt", "x")

# print("File Created Successfully" )

# https://www.youtube.com/watch?v=UCKbrAoFUlM

# **** Explain Exception handling****

# Palindrome: A palindrome number is a number that remains the same when digits are reversed.

print("Enter your number")
number = int(input())
temp = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

print(reverse)

if temp == reverse:
    print("Number is a palindrome")
else:
    print("Number is not a palindrome")


# Factorial


# if __name__ == "__main__":
#     number = int(input())
#     print("Enter your number")
#     factorial = 1

#     if number < 0:
#         print("Factorial of a negative number is not defined")

#     elif number == 0:
#         print(1)

#     else:
#         for i in range(1, number + 1):
#             factorial = factorial * i

#     print("The factorial of", number, "is", factorial)


# Armstrong

# n = int(input("Enter the number\n"))
# sum = 0
# order = len(str(n))
# copy_n = n

# while n < 0:
#     digit = n % 10
#     sum += digit**order
#     n = n // 10

#     if sum == copy_n:
#         print(f"{copy_n}It is an Armstrong Number")
#     else:
#         print(f"{copy_n}It is not an Armstrong Number")


# Fibonacci


# def fiboRecur(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fiboRecur(n - 1) + _fiboRecur(n - 2)


# if __name__ == "__main__":
#     num = int(input("Enter the number"))
#     print(f"Using recursion value of fib({num}) is {fiboRecur(num)}")

# Pattern


# for i in range(1, 6):
#     for j in range(1, i+1):
#         print('*', end= '')
#     print()


# for i in range(1, 6):
#     for j in range(1, 6-i+1):
#         print('*', end= '')
#     print()

# k=1
# for i in range(1, 6):
#     for j in range(1, 6-i+1):
#         print('*', end= '')
#         k+1
#     print()


# Python Pattern: Koi bhi pattern ho pehle '*' (star ke sath baniye) using matrix
# Jab pattern ban jaaye toh loop mai kuch bhi mat karo sirf printf ko use karke desired output nikalo


# ***Explain Recursion with proper example***


# ***Program to print the fib series***

#  Program to print the fibonacci sequence

# nterms = int(input("How many terms? "))

# n1, n2 =0, 1
# count =0

# # check if the number of terms is valid 
# if nterms <=0:
#     print("Please enter a valid number")

# elif nterms == 1:
#     print("Fibonacci sequence upto", nterms, ":")
#     print(n1)

# else:
#     print("Fibonacci Sequence:")
#     while count < nterms:
#         print(n1)
#         nth = n1 + n2
#         # Update values
#         n1 = n2
#         n2 = nth
#         count +=1
# ***Explain modules user defined and built-in***

# A module can define functions, classes, and variables. A module can also include runnable code. Grouping related code into a module makes the code easier to understand and use. It also makes the code logically organized.
# The user-defined module is written by the user at the time of program writing.
# Python Modules that are pre-defined are called built-in modules. We don’t have to create these modules in order to use them. Built-in modules are mostly written in C language. All built-in modules are available in the Python Standard Library

# ***Explain classes in Python***

# A class is a tool, like a blueprint or a template, for creating objects. It allows us to bundle data and functionality together.


# class Vehicle:
#     pass


# print(Vehicle)



string = input("Please Type something: ")

if string.count('_')>0:
    print("Not good")
else:
    print("Good")


#     def func(x, text):
#     print(x)
#     if text == '1':
#         print("Text is 1")
#     else:
#         print("Text is not 1")
        
# func("Nishi", '2')
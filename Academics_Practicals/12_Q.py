# 12) Python program to demonstrate string functions 

# 1. Compare Two Strings:

str1 = "Hello, world!"
str2 = "I love Python."
str3 = "Hello, world!"

# compare str1 and str2
print(str1 == str2)

# compare str1 and str3
print(str1 == str3)

# Output:
# False
# True



# 2. Join Two or More Strings:
greet = "Hello, "
name = "Jack"

# using + operator
result = greet + name
print(result)

# Output: Hello, Jack



# Iterate Through a Python String:

greet = 'Hello'

# iterating through greet string
for letter in greet:
    print(letter)


# Output:
# H
# e
# l
# l
# o  


# Python String Length:

greet = 'Hello'

# count length of greet string
print(len(greet))

# Output: 5



# String Membership Test:

print('a' in 'program') # True
print('at' not in 'battle') # False
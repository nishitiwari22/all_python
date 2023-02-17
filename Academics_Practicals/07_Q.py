# 7) Write a python program to demonstrate use of recursive function

# Example of a recursive function:

def factorial(n):
    """This is a recursive function
    to find the factorial of an integer"""

    if n == 1:
        return 1
    else:
        return (n * factorial(n-1))


num = 3
print("The factorial of", num, "is", factorial(num))

# Output: The factorial of 3 is 6
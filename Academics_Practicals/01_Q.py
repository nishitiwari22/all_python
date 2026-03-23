# Q1 a:Write a python program to convert Celsius to Fahrenheit.

celsius = float(input("Enter temperature in celsius: -"))

# This converts temperature from Celsius → Fahrenheit.
fahrenheit = (celsius * 9/5) + 32

# This uses old-style string formatting (% formatting).

# 🔍 Breakdown:
# 🧩 %2f
# %f → float (decimal number)
# 2 → minimum width (not very important here)

# 👉 Prints celsius as a float

print('%2f Celsius is : - %0.2f Fahrenheit' %(celsius, fahrenheit) )

How you can explain in interview:

# "The first line converts Celsius to Fahrenheit using the standard formula.
# The second line prints the result using old-style string formatting, where %f is used for floats and .2f limits the decimal precision. In modern Python, I would prefer using f-strings for better readability."

# c) Write a python program for Sum of squares of first n natural numbers.

# Solution:
n = int(input("Enter a number upto which you want to sum: "))
i = 1
sum = 0
for i in range(1, n+1):
    sum +=(i*i)
print("Sum of squares of first n natural numbers is", sum )

# Output:
# Enter a number upto which you want to sum: 5
# Sum of squares of first n natural numbers is  55



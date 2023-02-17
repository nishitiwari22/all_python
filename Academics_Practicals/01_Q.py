# Q1 a:Write a python program to convert Celsius to Fahrenheit.

celsius = float(input("Enter temperature in celsius: -"))
fahrenheit = (celsius * 9/5) + 32
print('%2f Celsius is : - %0.2f Fahrenheit' %(celsius, fahrenheit) )

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



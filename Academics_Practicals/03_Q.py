# Q3) Write a python program to calculate simple Interest and compound Interest.

# Solution:

# Reading principal amount, rate and time

principal = float(input('Enter principal amount: '))
time = float(input('Enter time: '))
rate = float(input('Enter rate: '))

# Calculation 

simple_interest = (principal*time*rate)/100
compound_interest = principal * ( (1+rate/100)**time - 1)

# Displaying result

print('The value of Simple interest is: %f' % (simple_interest))
print('The value of Compound interest is: %f' %(compound_interest))

# Output:
# Enter amount: 5000
# Enter time: 2
# Enter rate: 18
# Simple interest is: 1800.000000
# Compound interest is: 1962.000000
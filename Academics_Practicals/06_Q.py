# 6) Python Program to demonstrate operations on Tuples


a = (2, 4, 7, 5, 4)
b = (9, 1, 3, 5)

# 1) Membership Operators

# in
print(2 in a)
# Output: True

# not in 
print(2 not in a)
# Output: False


# 2) Concatenation

c = a + b
print(c)
# Output: (2, 4, 7, 5, 4, 9, 1, 3, 5)


# 3) Logical Operator

print(a == b)
# Output: False

print(a > b)
Output: False


# 4) Iteration

for x in a:
    print(x)


# 5) Nested tuple 

nested_tuple = (2, (54, 45), (25, (35, 65)))

print(nested_tuple[1][0])
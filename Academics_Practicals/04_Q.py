# Q4) Python Program to demonstrate operations on List.


# Solution:

# 1) Access elements of a list:
mix_list = [1, 'Jerry', 'Science', 79.5, True]

#access 1st element
print(mix_list[0])
#output: 1

#access 4th element
print(mix_list[3])
#output: 79.5

# *********************************************************************


# 2) Adding (or Appending) elements to a list:

sub_list = ['Python', 'Perl', 'Java', 'C++']
# Using insert 
sub_list.insert(3,'R')
print(sub_list)
# output: ['Python', 'Perl', 'Java', 'R', 'C++']

# Using append 
sub_list.append('Django')
print(sub_list)
# output: ['Python', 'Perl', 'Java', 'R', 'C++', 'Django']

# *********************************************************************


# 3) Sorting Lists:
sub_list = ['Python', 'Perl', 'Java', 'C++']

# ascending order 
sub_list.sort()
print(sub_list)
# Output: ['C++', 'Java', 'Perl', 'Python']

# descending order  
sub_list.sort(reverse = True)
print(sub_list)
# Output: ['Python', 'Perl', 'Java', 'C++']

# *********************************************************************


# 4) Update elements of a list:
mix_list = [1, 'Jerry', 'Science', 79.5, True]

#change science to computer using the index 
mix_list[2] = 'Computer'
print(mix_list)
#Output: [1, 'Jerry', 'Computer', 79.5, True]

# *********************************************************************


# 5) Delete elements of a list:
sub_list = ['Python', 'Perl', 'Java', 'C++']

#remove Java
sub_list.remove('Java')
print(sub_list)
#Output: ['Python', 'Perl', 'C++']

# *********************************************************************


# 6) Pop the elements of a list:
num_list = [1, 2, 3, 4]

#pop - Removes/pops out last element from the list and returns the remaining elements.
num_list.pop()
print(num_list)
# Output: [1, 2, 3]

# *********************************************************************


# 7) Length/Number of elements in a list:
num_list = [1, 3, 4, 5]

#length of a list  
print(len(num_list))
#Output: 4

# *********************************************************************


# 8) Maximum element within a list:
num_list = [1, 3, 4, 5]

# max in a list - for homogenous list 
max(num_list)
#Output: 5

# *********************************************************************


# 9) Concatenate lists:
num_list1 = [1, 3, 4, 5]
num_list2 = [5, 6, 7]

# concat lists 
print(num_list1 + num_list2)
#Output: [1, 3, 4, 5, 5, 6, 7]

# *********************************************************************


# 10) Iterating through a list:
num_list1 = [1, 3, 4, 5]

for element in num_list1: 
    print(element)
 
# Output:
# 1
# 3
# 4
# 5


# *********************************************************************

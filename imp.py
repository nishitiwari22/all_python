#  Some small random basic concepts.

# mUTABLE v/s Immutable


def changeList(li):
    li.appned(100)


def copyList(li):
    newLst = li[:]  # Copy of li
    newLst.append(100)
    return newLst


x = [1, 2, 3]
y = copyList(x)
print(x, y)


# IS OPERATOR (Checks whether two items are same in the memory)

lst = [1, 2, 3]
lst2 = lst
print(lst is lst2)

lst3 = lst[:]
print(lst is lst3)

print(id(lst), id(lst2), id(lst3))

#  When you make a copy wou get a new ID


# One correction: at 7:58 you are saying that when we create a new string x="str" and assign y=x , y  points to a new location but in reality y points to the same location as x.
# Only if we change y then will y point to a different location. See the code below.


x = "str"
y = x
print(x is y)
y = "newStr"
print("x is", x, "and", "y is ", y)


# output:​
# True
# x is str and y is  newStr


# Please correct me if i am wrong


x = "str"
y = x
id(y) == id(x)
# True

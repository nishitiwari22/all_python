x = [x for x in range(5)]
print(x)


x = [x + 5 for x in range(5)]
print(x)

x = [[0 for x in range(100)] for x in range(5)]
print(x)


x = [i for i in range(100) if i % 5 == 0]
print(x)

x = {i for i in range(100) if i % 5 == 0}  #  I made it a dictionary
print(x)


x = tuple(
    i for i in range(100) if i % 5 == 0
)  # Made it a tuple by adding the keyword tuple
print(x)


# Unpack Operator *args & **kwargs
# You can put a function inside a function it is valid

#  The below stuff is little advanced
def func(x):
    def func2():
        print(x)

    return func2


x = func(3)
x()


#  Unpack Operator separates all of the element from the list into individual elements


def func(*args, **kwargs):
    pass


x = [1, 23, 45, 87]
print(*x)


def func(x, y):
    print(x, y)


pairs = [(1, 2), (3, 4)]

for pair in pairs:
    func(*pair)
#  For dictionary we will need two astricks

for pair in pairs:
    func(**{"x": 2, "y": 5})


def func(*args, **kwargs):
    print(*args)


func(1, 2, 3, 4, 5, one=0, two=1)

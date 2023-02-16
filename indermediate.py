#**** Optional Parameters Tut 1****

# def func(x):
#     return x**2

# call = func (5)
# print(call)


# def func2(word, frequency):
#     print(word * frequency)

# call = func2 ('nishi ', 10)

# def func2 (word, add=5, freq=1):
#     print(word * (freq+add))

# call = func2 ('nishi ', 5, 2)

# I not at all understood the below code

class car(object):
    def __init__(self, make, model, year, condition='New', kms=0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms

    def display (self, showAll = True):
        if showAll:
            print("This car is a %s %s from %s,  it is %s and has %s kms." %(self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s from %s."   %(self.make, self.model, self.year))

whip = car('Ford', 'Fusion', 2012)
whip.display(False)

#**** Static and Class Methods Tut 2****

class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def isAdult(age):
        return age >= 18
    
    def display(self):
        print(self.name, 'is', self.age, 'years old')


newPerson = person('tim', 18)
print(person.getPopulation())

# Map function tut 3

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def func(x):
    return x**x


newList = []
for x in li:
    newList.append(func(x))

print(newList)



# Filter Function tut 4

def add7(x):
    return x+7

def isOdd(x):
    return 1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

b = list(filter(isOdd,a))

c= list(map(add7,filter(isOdd,a )))


# Lambda Function


def func(x):
    return x+5

func2 = lambda x: x+5
print(func2(9))
print(func2)


def func(x):
    func2 = lambda x: x+5
    return x+5

    return func2(x) + 85

func3 = lambda x, y = 4: x+y
print(func3(5))

print(func2)

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newList = list(map(lambda x: x+5, a))
print(newList)
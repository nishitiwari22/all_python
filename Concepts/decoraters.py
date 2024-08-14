
# https://youtu.be/JgxCY-tbWHA?si=WZ6CMdncL6858uXK

# Decorator (Function that modifies another function)

import time

def timer(func):
    def wrappper(*args, **kwargs): #args - any number of positional arguments | #kwargs: any number of keyword arguments 
        start_time = time.time() # Start time
        result = func(*args, **kwargs) # Call the decorated function
        end_time = time.time() # End time
        print(f"Function {func.__name__!r} took: {end_time - start_time:.4f} sec")
        return result

    return wrappper

@timer
def example_function(n):
    return f"The sun is {sum(range(n))}"


example_function = timer(example_function)

print(example_function(100000000))

######

class Circle: 
    def __init__(self, radius):
        self._radius = radius # It should be treated as private 

    @property 
    def radius(self):
        """Get the radius of the circle."""
        return self._radius # Return the value of the private attribute radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the circle. Must be positive."""
        if value >= 0
            self._radius = value
        else:
            raise ValueError("Radius must be positive")


    @property
    def diameter(self):
        """Get the diameter of the circle."""
        return self._radius * 2


# Usage 
c = Circle(5)
print(c.radius) # 5
print(c.diameter) #10
c.radius = 10
print(c.radius) # 10
print(c.diameter) # 20 

#####

class Math:
    @staticmethod  # Use to denote a method inside of a class as static  
    def add(x,y):
        return x + y

    @staticmethod
    def multiple(x,y):
        return x + y

# Usage 
print(Math.add(5, 7)) # 12
print(Math.multiply(3, 4)) # 12

#### 

class Person: 
    species = "Homo Sapiens"

    @classmethod
    def get_species(cls):
        return cls.species

#Usage 
print(Person.get_species()) # Homo sapiens


#### 

import functools

#  Calculating the calculated number again and again not good

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(10))

######

import functools

# Allows us to cache the result 

def fibonacci(n, cache={}):
    if n in cache:
        return cache[n]

    if n == 0:
        return 0 
    elif n == 1: 
        return 1

    cache[n] = fibonacci(n - 1, cache) + fibonacci(n - 2, cache)
    return cache[n]

print(fibonacci(40))


######

import functools

@functools.cache
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(40))


########

class Product: 
    def __init__(self, name: str, price: float, quantity: int = 0):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_cost(self) -> float:
        return self.price * self.quantity

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity})"
        )

    def __eq__(self, other):
        if not isinstance(other, Product):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return (
            self.name == other.name
            and self.price == other.price
            and self.quantity == other.quantity
        )


######

from dataclasses import dataclasses

@dataclass
class Product:
    name: str
    price: float
    quantity: int = 0 

    def total_cost(self) -> float:
        return self.price * self.quantity

p1 = Product(name="Laptop", price=1000.0, quantity=3)
p2 = Product(name="Laptop", price=1000.0, quantity=3)
p3 = Product(name="Smartphone", price=5000.0, quantity=2)

print(p1)  # Product(name="Laptop", price=1000.0, quantity=3)
print(p1.total_cost()) # 3000.0
print(p1 == p2) # True 
print(p1 == p3) # False





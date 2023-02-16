# Random Basic Stuff
# # y = 1
# # print(type(y))
# # This will give output 'int'


# # def hello():
# #     print("hello")
# #  This will give output function


# string = "hello"
# print(string.upper())

# z = 1
# print(z.upper())
# #  AttributeError: 'int' object has no attribute 'upper'
# # x = 1
# # print(type(hello))


# ***Start From Here*****


# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         # print(name)
#         self.age = age

#     # def bark(self):
#     # print("bark")
#     def get_name(self):
#         return self.name

#     def get_age(self):
#         return self.age

# def add_one(self, x):
#     return x + 1

# def set_age(self, age):
#     self.age = age


# d = Dog("sheru", 12)
# d.set_age(12)
# print(d.get_age())
# d2 = Dog("kiggo", 7)
# d2.set_age(7)
# print(d2.get_age())
# d.bark()

# print(d.add_one(5))


# Method is essentially a function that goes inside  of a class easiest way to define it
# We can make methods that have different arguments assocaited with them or parameters with them.


# from matplotlib.bezier import NonIntersectingPathException


# class Student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade  # 0 - 100

#     def get_grade(self):
#         return self.grade


# class Course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []

#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False

#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()

#         return value / len(self.students)


# s1 = Student("Nishi", 20, 100)
# s2 = Student("Sabika", 20, 78)
# s3 = Student("Sabika", 20, 78)

# course = Course("Science")
# course.add_student(s1)
# course.add_student(s2)
# print(course.add_student(s3))
# print(course.get_average_grade)


# class Student_Harry_Bhai_video:
#     pass


# sabika = Student_Harry_Bhai_video()
# nishi = Student_Harry_Bhai_video()

# nishi.name = "Nishi"
# nishi.std = 14
# nishi.section = 1
# sabika.section = 13
# sabika.subjects = ["hindi"]
# print(nishi.section, sabika.subjects)



# ***Oops****

# class Shiv:
#     def Lands(self):
#         print("Having 50 Acre Lands")

# class Daughter(Shiv):
#     def Money(self):
#         print("Having 10 Lakhs Money")

# D=Daughter()
# D.Lands
# D.Money()

class Father:
    def Lands(self):
        print("Having 50 Acre Lands")

class Son(Father):
    def Money(self):
        print("Having 10 Lakhs Money")

# S=Son()
F=Father()
F.Lands
# S.Money()
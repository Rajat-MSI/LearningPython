# python class

# a class is a user-defined data type that contains both the data itself and
# the methods that may be used to manipulate it

class Person:
    def __init__(self,p_id,name,age):

        # this is constructor that is called when as new person object created
        self.p_id = p_id
        self.name = name
        self.age = age

    def greet(self):
        # this method is of person class
        print("hello this is:",self.name)

# creating object of person
person = Person("10","person_name",20)
# calling class function
person.greet()

# self parameter
# it refers to the current instance of the class and accesses the class
# variables self should be first parameter of any function belongs to a class


# __init__ method
# it is constructor in python it is used to initialize instance variables

# class variables
# class variable is a variable is shared among all instances of a class just
# like static in java

# instance variables
# an instance variable is unique to each object (instance) created from class
# It is usually defined using self inside the __init__() method

class Student:
    # class variable
    school = "student_school"

    def __init__(self,name,age):
        # instance variable
        self.name = name
        self.age = age

    def get_student(self):
        print("student_name:",self.name)
        print("student_age:",self.age)
        print("school:",self.age)

# --------------------------------------------------------------------------

# static method and static blocks in python

# A static method is a function inside a class that doesn’t need the object
# or class to do its job because  static methods are not dependent on any
# object-specific or class-specific data.

# python doesn't have static initialization blocks like java
print("\n* static method")
class MathTool:
    @staticmethod
    def multiply(x,y):
        return x * y

# no need to created object we will directly call static method using class
print("called static method - 2 x 3 =",MathTool.multiply(2,3))


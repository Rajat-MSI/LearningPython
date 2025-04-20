# python polymorphism

# one method name, many forms

# 1.function overloading
# 2.function overriding
# 3.duck typing
# 4.operator overloading

# 1.function overloading
# it is not possible in python but can be implemented using *args and **kwargs

# --------------------------------------------------------------------------

# 2.function overriding
# child class method redefines parent method
print("* function overriding")
class Animal:
    def speak(self):
        print("animal speaking")

class Dog(Animal):

    # this method is getting overridden
    def speak(self):
        print("dog barking")

# creating parent class object
animal = Animal()
print("calling speak() from parent:")
animal.speak()
# creating child class object
print("calling speak() from child:")
dog = Dog()
dog.speak()

# --------------------------------------------------------------------------

# 3.duck typing
# it is a concept in Python where the type of an object is determined by its
# behavior (methods & properties) rather than its actual class or inheritance
print("\n* duck typing")
class Pen:
    def write(self):
        print("writing with a pen")

class Pencil:
    def write(self):
        print("writing with a pencil")

class Eraser:
    def write(self):
        print("erasing something")

def use_tool(tool):
    tool.write()

pen = Pen()
pencil = Pencil()

print("calling write() from class Pen:")
use_tool(pen)
print("calling write() from class Pencil:")
use_tool(pencil)

# key points
# python doesn't check the type of object explicitly in duck typing
# it only cares if the object has the required method/attribute
# it makes code more flexible and reusable
# reduces the need for big inheritance trees
# common in functions or classes that work with many different types

# --------------------------------------------------------------------------

# 4.operator overloading
# it allows us to define custom behavior for built-in operators
# python internally calls a special method when using an operator:
# operator	method
# +	        __add__()
# -	        __sub__()
# *	        __mul__()
# ==	    __eq__()
# <	        __lt__()
# >	        __gt__()
# //	    __floordiv__()
# %	        __mod__()
# **	    __pow__()

print("\n* operator overloading")

class Book:
    def __init__(self,pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages

# initialized book1 pages
book1 = Book(150)
# initialized book2 pages
book2 = Book(100)

# make sure we are not adding pages variable here we are adding objects
total_pages = book1 + book2
print("added book1 and book2 objects:",total_pages)

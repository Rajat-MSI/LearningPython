# python inheritance

# inheritance provides code reusability to the program because we can use
# existing properties of a base class to create a child class
# inheritance is 'is a' relationship

# in python, a derived class can inherit base class by just mentioning the
# base in the bracket after the derived class name

# 1.single inheritance
# 2.multiple inheritance
# 3.multilevel inheritance
# 4.hierarchical inheritance
# 5.hybrid inheritance

# --------------------------------------------------------------------------

# 1.single inheritance

print("* single inheritance")
class Animal:
    name = ""
    def walk(self):
        print("animal walks")

class Dog(Animal):
    def walk(self):
        print(self.name,"is walking")

# created object of class animal (parent class)
animal = Animal()
print("parent animal walks:",end=" ")
animal.walk()

# created object of class dog (child of animal)
dog = Dog()
setattr(dog,"name","dog")
print("child dog walks:",end=" ")
dog.walk()

# --------------------------------------------------------------------------

# super() function in python
# if we need to access the superclass method from the subclass,
# we use the super() function
print("\n* super() function")
class Animal:
    name = ""
    def walk(self):
        print("animal walks")

class Dog(Animal):
    def walk(self):
        print("using super() called walk() from parent")
        super().walk()
        print(self.name,"is walking")

# created object of class animal (parent class)
animal = Animal()
print("parent animal walks:",end=" ")
animal.walk()
# created object of class dog (child of animal)
dog = Dog()
setattr(dog,"name","dog")
print("child dog walks:")
dog.walk()

# --------------------------------------------------------------------------

# 2.multiple inheritance
print("\n* multiple inheritance")
class Mammal:
    type = ""
    def mammal_info(self):
        print("mammal can give direct birth")

class WingedAnimal:
    name = ""
    def winged_animal_info(self):
        print("winged animal can fly")

class Bat(Mammal,WingedAnimal):
    def bat_info(self):
        print("mammal type:",self.type)
        print("animal name:",self.name)

# created object of first parent class
mammal = Mammal()
print("calling from Mammal:")
mammal.mammal_info()

# created object of second parent class
animal = WingedAnimal()
print("calling from WingedAnimal:")
animal.winged_animal_info()

# created object of child class inheriting from both parent class
bat = Bat()
setattr(bat,"type","winged animal")
setattr(bat,"name","bat")
print("calling from Bat:")
bat.bat_info()

# method resolution order (MRO)
# if two superclasses have the same method (function) name and the derived
# class calls that method, Python uses the MRO to search for the right
# method to call

# MRO (method resolution order) is the order in which Python searches for
# a method or attribute when it's called on an object. It determines
# which method gets executed first in a class hierarchy
# Python uses the C3 linearization Algorithm to figure out the order

print("\n* method resolution order (MRO)")
class Parent1:
    def info(self):
        print("this is parent1")

class Parent2:
    def info(self):
        print("this is parent2")

class Child(Parent1,Parent2):
    def get(self):
        print("this is child of parent1 and parent2")

# calling info() from child so confusion is from which parent info() will be
# called
child = Child()
child.info()

# python prioritize the parent class by (working of C3 linearization algo):
# * Putting the current class first
# * Looking left to right in the base classes
# * Maintaining local precedence ordering
# * Ensuring that children come before parents

# --------------------------------------------------------------------------

# 3.multilevel inheritance
print("\n* multilevel inheritance")
class Level1:
    def info(self):
        print("this is parent class Level1")

class Level2(Level1):
    def info(self):
        print("this is child class of Level1")

class Level3(Level2):
    def info(self):
        print("this is child class of Level2")

# creating object of parent class
level_1 = Level1()
level_1.info()
# creating object of child class of level_1
level_2 = Level2()
level_2.info()
# creating object of child class of level_2
level_3 = Level3()
level_3.info()

# --------------------------------------------------------------------------

# 4.hierarchical inheritance
print("\n* hierarchical inheritance")
class Animal:
    name = ""
    def walk(self):
        print(self.name,"animal is walking")

class Dog(Animal):
    def walk(self):
        print(self.name,"dog is walking")

class Cat(Animal):
    def walk(self):
        print(self.name,"cat is walking")

# creating object of parent
animal = Animal()
setattr(animal,"name","unknown")
print("calling parent animal:")
animal.walk()
# creating object of first child inheriting from parent
dog = Dog()
setattr(dog,"name","bruno")
print("calling child dog:")
dog.walk()
# creating object of second child inheriting from parent
cat = Cat()
setattr(cat,"name","tabby")
print("calling child cat:")
cat.walk()

# --------------------------------------------------------------------------

# 5.hybrid inheritance
# combination of all other types of inheritance

# --------------------------------------------------------------------------

# python aggregation

# aggregation is a concept in which an object of one class can
# own or access another independent object of another class
# aggregation is 'has a' relationship

print("\n* python aggregation")
class Student:
    def __init__(self,s_id,name,age,address):
        self.s_id = s_id
        self.name = name
        self.age = age
        self.address = address

class Address:
    country = "USA"
    def __init__(self,street,state):
        self.street = street
        self.state = state

# creating address object
address = Address("22nd becker street","north dakota")
# creating student object and passing address as object
student = Student(100,"tony stark",23,address)
print("student details")
print("s_id:",getattr(student,"s_id"))
print("name:",getattr(student,"name"))
print("age:",getattr(student,"age"))

# getting student address from address class
print("\nstudent address details")
student_address = getattr(student,"address")
print("street:",getattr(student_address,"street"))
print("state:",getattr(student_address,"state"))
print("country:",getattr(student_address,"country"))
# --------------------------------------------------------------------------

# inheritance methods
print("\n* inheritance methods")

# 1.issubclass(sub_class,sup_class)
# it is used to check the relationships between the specified classes

# 2.isinstance (obj, class)
# is used to check the relationship between the objects and classes

print("issubclass(Cat,Animal):",issubclass(Cat,Animal))
print("isinstance(cat,Cat):",isinstance(cat,Cat))


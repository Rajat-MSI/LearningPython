# python abstraction

# abstraction is used to hide the irrelevant data/class in order to reduce
# the complexity

# we need to import the abc module, which provides the base for defining
# abstract base classes (ABC). The ABC works by decorating methods of the
# base class as abstract

# we use the @abstractmethod decorator to define an abstract method or if
# we don't provide the definition to the method, it automatically becomes
# the abstract method

# importing abstract base class for abstraction
from abc import ABC, abstractmethod

# we inherit ABC to our class
class Animal(ABC):
    # creating abstract method
    @abstractmethod
    def sound(self):
        pass

# implemented animal in child class Dog
class Dog(Animal):
    def sound(self):
        print("Bark")

# implemented animal in child class Cat
class Cat(Animal):
    def sound(self):
        print("Meow")

# cannot create instance of abstract class
# animal = Animal()

# creating object of child class dog
dog = Dog()
print("calling child class dog:")
dog.sound()
# creating object of child class cat
cat = Cat()
print("calling child class cat:")
cat.sound()

# note: if a class has both abstract and non abstract methods in class then
# it is abstract class in python
# if a class has only abstract methods then it is interface in python
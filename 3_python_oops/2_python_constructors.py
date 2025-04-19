# python constructor

# a constructor is a method which is used to initialize class instance members
# we use __init__() to create a constructor it accept self as first argument

# def __init__(self,name,age):
#     self.name = name
#     self.age = age

# python non parameterized constructor
# it has only self as an argument it does not manipulate instance variable

print("* non parameterized constructor")
class Student:
    name = "student_name"
    age = 22

    def display(self):
        print("student_name:",self.name)
        print("student_age:",self.age)

student = Student()
student.display()

# python parameterized constructor
# it has multiple parameters with self and use to manipulate instance variable

print("\n* parameterized constructor")
class Employee:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print("student_name:",self.name)
        print("student_age:",self.age)

employee = Employee("employee_name",24)
employee.display()

# default constructor
# when we do not create constructor but create an object of class default
# constructor gets automatically created and called

# note: the constructor overloading is not allowed in python


# python built-in class functions

# getattr(obj_name,attr_name)
# setattr(obj_name,attr_name,attr_value)
# delattr(obj_name,attr_name)
# hasattr(obj_name,attr_name)

print("\n* python built-in class functions")
class Student:
    school = "default_school_name"
    def __init__(self,s_id,name,age):
        self.s_id = s_id
        self.name = name
        self.age = age

student_1 = Student(101,"student_name_1",22)
student_2 = Student(105,"student_name_2",26)

print("student_1 details:")
print("student_id:",getattr(student_1,"s_id"))
print("student_name:",getattr(student_1,"name"))
print("student_age:",getattr(student_1,"age"))

# updating student_1 details
setattr(student_1,"s_id",104)
setattr(student_1,"name","new_student_name_1")
setattr(student_1,"age",23)

print("\n* called setattr() and updated student_1 details")
print("student_1 updated details:")
print("student_id:",getattr(student_1,"s_id"))
print("student_name:",getattr(student_1,"name"))
print("student_age:",getattr(student_1,"age"))

print("\n* deleted age attr from: student_1.__delattr__('age')")
delattr(student_1,"age")
try:
    print("student_age:",getattr(student_1,"age"))
except:
    print("age attribute not present in student_1")

print("does student_1 has age attribute:",hasattr(student_1,"age"))

print("\n* student_2 details:")
print("student_id:",getattr(student_2,"s_id"))
print("student_name:",getattr(student_2,"name"))
print("age is present in student_2:",getattr(student_2,"age"))

# below is another method to get,set,del attribute for a class
# it is more low level and less safe

# setting
# student_1.__setattr__("s_id",104)
# student_1.__setattr__("name","new_student_name_1")
# student_1.__setattr__("age",23)

# getting
# print("\n* student_2 details:")
# print("student_id:",student_2.__getattribute__("s_id"))
# print("student_name:",student_2.__getattribute__("name"))
# print("age is present in student_2:",student_2.__getattribute__("age"))

# deleting
# print("\n* deleted age attr from: student_1.__delattr__('age')")
# student_1.__delattr__("age")
# try:
#     print("student_age:",student_1.__getattribute__("age"))
# except:
#     print("age attribute not present in student_1")


# built in class attributes
# 1.__dict__
# 2.__doc__
# 3.__name__
# 4.__module__
# 5.__bases__

# 1.__dict__
# It provides the dictionary containing the information about the class
# 2.__doc__
# It contains a string which has the class documentation
# 3.__name__
# It is used to access the class name
# 4.__module__
# It is used to access the module in which, this class is defined
# 5.__bases__
# It contains a tuple including all base classes

print("\n* built in class attributes")
print("student_1.__dict__:",student_1.__dict__)
print("student_1.__doc__:",student_1.__doc__)
print("student_1.__module__:",student_1.__module__)


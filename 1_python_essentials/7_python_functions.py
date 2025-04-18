# python functions

# in python all parameters are passed by reference

# function to determine string is palindrome or not
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

s = "malayalam"
print("is_palindrome:",is_palindrome(s))


# function arguments
# 1.default arguments
# 2.keyword arguments
# 3.required arguments
# 4.variable-length arguments

# 1.default arguments
# it allows to assign a default value to a function parameter so when the
# function is called without that argument, the default value is used
print("\n* default arguments")
def function_1(num1,num2 = 30):
    print("num1:",num1)
    print("num2:",num2)

print("passing only one argument function(10)")
function_1(10)

print("passing two arguments function(10,20)")
function_1(10,20)

# 2.keyword arguments
# are used when calling a function we explicitly mention the name of the
# parameter along with its value
print("\n* keyword arguments")
def function_2(num1,num2):
    print("num1:",num1)
    print("num2:",num2)

print("without using keyword function(10,20)")
function_2(10,20)
print("with using keyword function(num1=10,num2=20)")
function_2(num1=10,num2=20)
print("with using keyword function(num2=10,num1=20)")
function_2(num2=10,num1=20)

# 3.required arguments
# are those that must be passed to the function in the correct position
# and number if we miss them, python will throw an error
print("\n* required arguments")
def function_3(num1,num2):
    print("num1:",num1)
    print("num2:",num2)

print("passing all the arguments")
function_3(10,20)
print("passing only one argument (it will throw error)")
try:
    function_3(10)
except:
    print("less arguments in function")

# 4.variable-length arguments
# *args → collects extra positional arguments into a tuple
# **kwargs → collects extra keyword arguments into a dictionary
print("\n* variable-length arguments")
def function_4(*args):
    total = 0
    for i in args:
        total +=  i
    print("sum:",total)

print("using *args to pass multiple arguments as tuple")
function_4(10,20,30,40) # passing multiple arguments

def function_5(**kwargs):
    for i in kwargs.items():
        print(i)

print("using **kwargs to pass multiple arguments as dictionary")
function_5(name = "python",alias = "programming language")
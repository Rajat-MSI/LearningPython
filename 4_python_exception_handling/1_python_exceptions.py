# python exceptions

# python exceptions provide a mechanism for handling errors that occur during
# the execution of a program

# * raising an exception
# we can raise exception using raise keyword and class Exception with a
# custom message

print("* raising exception - raise keyword")
age = 18
print("your age:",age)
if age < 18:
    raise Exception("you have to be at least 18 for voting rights")

# here the program execution will be halted if exception occurs

# --------------------------------------------------------------------------

# * assert keyword

# python offers a specific exception type that you should only use when
# debugging your program during development. This exception is the
# AssertionError
# use the assert keyword to check whether a condition is met and let Python
# raise the AssertionError if the condition isn’t met

print("\n* AssertError - assert keyword")
age = 15
print("your age:",age)
assert (age < 18), "you have to be at least 18 for voting rights"

# here the program will not be halted if AssertionError gets occur

# --------------------------------------------------------------------------

# * try and except

# we use try and except block to catch and handle exceptions.
# Python executes code following the try statement as a normal part of the
# program. The code that follows the except statement is the program’s
# response to any exceptions

# try:
#     normal code
# except:
#     code when exception occurs

print("\n* try and except block")
# trying to divide 0 with 0
try:
    print("try block")
    division = 0/0      # exception will occur
    print("result:",division)
except:
    print("except block")
    print("cannot divide 0 with 0")

# --------------------------------------------------------------------------

# * proceeding after a successful try with else

# we can use python  else statement to instruct a program to execute a certain
# block of code only in the absence of exceptions
print("\n* try except and else block")
try:
    division = 12//2
    print("result:",division)
except:
    print("exception occurred")
else:
    # since no exception occurred then print success message
    print("division successfully executed")

print(ZeroDivisionError)

# --------------------------------------------------------------------------

# * cleaning up after execution with finally

# python will execute everything in the finally clause. It doesn’t matter
# if you encounter an exception somewhere in any of the try … except blocks

print("\n* try except else and finally block")

try:
    numerator = 10
    denominator = 0
    result = numerator//denominator
    print("result:",result)
except:
    print("cannot divide change the values")
else:
    numerator = 10
    denominator = 5
    result = numerator//denominator
    print("result:",result)
finally:
    # cleanup code
    del numerator
    del denominator
    print("variable memory de-allocated")

# --------------------------------------------------------------------------

# * errors and exceptions in python

# errors are concrete conditions, such as syntax and logical errors
# for example - invalid syntax

# exceptions are events that interrupt the execution of a program
# for example - getting a file that does not exist
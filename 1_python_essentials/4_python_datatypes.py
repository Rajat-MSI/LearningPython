# python datatypes
# 1 - numeric types - int,float,complex
# 2 - sequence types - str,list,tuple,range
# 3 - set types - set,frozenset
# 4 - mapping types - dict
# 5 - boolean types - bool
# 6 - binary types - bytes,bytearray,memory view
# 7 - none type - none

# 1 - numeric types
# integer - represented by 'int' class can store signed integers
# in python there is not limit to length of integer value the value can be of
# any length and can reach the maximum available memory system

# float - represented by 'float' class can store decimal point or numbers
# in scientific notation it follows IEEE 754 floating point standard and
# has precision limit up to 15 decimal points

# complex numbers - present by 'complex' class consisting of a real part
# and an imaginary part 'a+bj'
# a - represent either float or integer
# b - represent imaginary part can be either float or integer
# j - represent  √(-1). It is an imaginary unit used in Python


# 2 - sequence data types
# list [] - represented by 'list' class similar to array in other languages
# it is ordered, mutable and can store elements of different datatypes

# tuple () - represented by 'tuple' class store elements in order and it is
# immutable

# str '',"",""" - are sequence of characters represented by 'str' class
#  it is also immutable like tuples

# range() - is a sequence datatype represents sequence of numbers from
# a starting to ending value incrementing a particular value
print("* creating range")
r = range(2,24,2)
print("range:", r)
print("range as list:",list(r))


# 3 - set data types
# set {},set() - is unordered, mutable and un-indexed collection of unique
# elements it performs operations like union,intersection,difference

# frozenset() - is immutable,unordered datatype it consist of unique items
# it is like normal set but it is immutable like tuple
print("\n* creating frozenset")
p_list = [10,20,30,30,20,10]
p_frozenset = frozenset(p_list)
print("p_list:", p_list)
print("p_list as frozenset:", p_frozenset)


# 4 - mapping datatype - dictionary
# dict - stores element in key-value pairs it is ordered and keys are unique


# 5 - boolean datatype
# True - represents 1
# False - represents 0


# 6 - binary datatypes
# python has it to handle raw binary data

# bytes - is an immutable sequence of bytes ranging from 0 to 255.
# it is useful for working with binary files,network communication,cryptographic
# functions
print("\n* creating bytes in python")
byte_list = bytes([82,65,74,65,84]) # ASCII values
print("value of bytes:", byte_list)

# bytearray - is mutable sequence of bytes that allows modification of
# binary data in place
print("\n* creating bytearray in python")
bytearray_list = bytes([82,65,74,65,84]) # ASCII values
print("value of bytearray:", bytearray_list)

# memoryview - is used to provide a lightweight and efficient way to access
# binary data without copying it. it is useful for large data operations where
# performance is relevant
print("\n* creating memoryview object")
memoryview1 = memoryview(byte_list)
memoryview2 = memoryview(bytearray_list)
print("byte_list:", memoryview1)
print("bytearray_list:", memoryview2)


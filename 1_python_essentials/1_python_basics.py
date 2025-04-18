# This is a comment in python

# python keywords
import keyword
print(keyword.kwlist)

# python literals

# numeric - int,float,complex numbers
# integer
decimal_num = 10
binary_num = 0b1010 # Prefixed with 0b or 0B
octal_num = 0o12 # Prefixed with 0o or 0O
hexadecimal_num = 0xA # Prefixed with 0x or 0X
print("\n* all will print integer 10")
print("decimal_num:", decimal_num)
print("binary_num:", binary_num)
print("octal_num:", octal_num)
print("hexadecimal_num:", hexadecimal_num)

#floating
float_num = 20.5
scientific_num = 2.5e3
negative_float = -0.99
print("\n* floating point number")
print("float_num:", float_num)
print("scientific_num:", scientific_num)
print("negative_float:", negative_float)

#complex
complex_num = 5+3j
print("\n* complex number")
print("real part:", complex_num.real)
print("imaginary part:", complex_num.imag)

# String - any set of characters written in string quotes
# single line strings
print("\n* single line string")
single_quoted_string = 'Hello World'
double_quoted_string = "Hello World"
print("single_string:", single_quoted_string)
print("double_string:", double_quoted_string)

# multi line strings
print("\n* multi line string")
multi_line_string = """This is a multi-line string
It can span multiple lines. 
Useful for documentation and long texts.
"""
print(multi_line_string)

# escape characters in strings
# \n newline
# \t tab
# \' single quote
# \" double quote
# \\ backslash

# string concatenation and repetition
print("* string concatenation and repetition")
string1 = "Hello"
string2 = "World"
concatenated = string1 + string2
repeated = string1 * 3
print("concatenated:", concatenated)
print("repeated:", repeated)

# boolean - True or False
print("\n* boolean values")
is_palindrome = True
is_raining = False
print("is_palindrome:", is_palindrome)
print("is_raining:", is_raining)

# collection - list, tuple, dictionaries and set
# list - ordered and mutable collection [1,2,3]
print("\n* python collections")
p_list = [10,20,30,20]
print("python list:",p_list )

# tuple - ordered and immutable collection (1,2,3)
p_tuple = (10,20,30,20)
print("python tuple:",p_tuple )

# dictionary - key-value paris {'subject':'python','marks':90}
p_dict = {
    'subject' : 'python',
    'marks' : 100
}
print("python dict:",p_dict )

# set - unordered collection of unique items {1,2,3}
p_set = {10,20,30,40}
print("python set:",p_set )

# special literal - None
# It represents absence of value or in simple null
print("\n* special literal")
value = None
print("printing variable value:", value)
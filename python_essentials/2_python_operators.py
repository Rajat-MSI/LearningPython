# python operator

# arithmatic operators
print("\n* arithmatic operators")
# addition
a = 10
b = 20
print("addition:", a+b)

# subtraction
print("subtraction:", a-b)

# multiplication
print("multiplication:", a*b)

# division
a = 20
b = 2
print("division:", a/b)

# floor division - it provides quotients floor value obtained by division
print("floor division:", a//b)

# reminder
print("reminder:", a%b)

# exponent
a = 2
b = 5
print("exponent:",a**b)

# comparison operators
# == - equal to
# != - not equal to
# > - greater than
# < - less than
# >= - greater than equal to
# <= - less than equal to

# assignment operators
print("\n* assignment operators")
a = 12
b = 2
print('a += b:', a + b)
print('a -= b:', a - b)
print('a *= b:', a * b)
print('a /= b:', a / b)
print('a %= b:', a % b)
print('a **= b:', a ** b)
print('a //= b:', a // b)

# logical operators
# and
# or
# not

# bitwise operators
# & - bitwise and
# | - bitwise or
# ^ - bitwise xor
# ~ - bitwise not
# << - bitwise left shift
# >> - bitwise right shift

# membership operators
# in
# not in
print("\n* membership operators")
p_list = [10,20,30,40,50]
print(p_list)
x = 10
if x in p_list:
    print(x, "is present")
else:
    print(x, "10 is not present")

# identity operators
print("\n* identity operators")
a = 10
b = 20
print("a is b?", a is b)
print("a is not b?", a is not b)

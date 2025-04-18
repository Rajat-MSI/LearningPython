# python variables

# dynamic typing
# python variables are dynamically which means we can store different
# types of value in the same variable
print("* dynamic assigment")
var1 = 21
var1 = "python"
print("value of var1:", var1)

# multiple assignment
# we can assign values to multiple variables in a single line
print("\n* multiple assigment 1")
var1 = var2 = var3 = "python programming language"
print("value of var1:", var1)
print("value of var2:", var2)
print("value of var3:", var3)

# assigning different value to multiple variables
print("\n* assigning different value to multiple variables")
var1,var2,var3 = 100,"python","java"
print("value of var1:", var1)
print("value of var2:", var2)
print("value of var3:", var3)

#type casting python
print("\n* type casting")
# integer
var1 = 9
print("integer:", var1)

# implicit type casting - we will get a float
var2 = var1/4
print("implicit type casting:", var2)

# explicit type casting - float will be cast back to int
var2 = int(var2)
print("explicit type casting:", var2)

# getting type of variable or object
print("\n* type of variable or object")
p_list = [10,20,30]
a = 10
language = "python"
print("variable p_list:", type(p_list))
print("variable a:", type(a))
print("variable language:", type(language))

# deleting variable in python
print("* deleting variable")
a = 20
print("printing a:", a)
# this will delete variable a
del a
# below statement will throw error
# print("printing a:", a)

# ** click here to know about object reference https://1drv.ms/w/s!Au5n0-NUYaQLgqQwPKwS3yuiiHrVlw?e=CCyLuc
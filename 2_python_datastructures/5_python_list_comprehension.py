# python list comprehension

# it is a shorter and cleaner way to create a list from another list or
# iterable using a single line of code it is like for loop + if condition

# syntax: n_list = [expression for item in iterable if condition == True]

# iterate through string
print("\n* iterate through string")
l_list = [i for i in 'python']
print(l_list)

# using condition in list comprehension
print("\n* using condition in list comprehension")
p_list = [1,2,3,4,5,6,7,8,9,10]
n_list = [i for i in p_list if i % 2 == 0]
print("p_list:",p_list)
print("n_list:",n_list)

# * python tuple
from itertools import count

# we create tuple using brackets ()
# it is ordered which means tuple maintains the order of insertion
# tuple is immutable which means it does not allow modification after creation
# tuple is heterogeneous which me it can store elements of multiple data types

# * operations on tuple
# 1.creation
# 2.accessing element
# 3.slicing tuple
# 4.deleting tuple
# 5.modifying tuple
# 6.adding tuple to a tuple
# 7.packing and unpacking tuple
# 8.looping tuples
# 9.concatenating tuples
# 10.repetition tuples
# 11.membership

# 1.creation
print("\n* creating tuple")

p_tuple = (25,"hello",88.728,"world",False)
print("p_tuple:",p_tuple)

# 2.accessing element
print("\n* accessing tuple element")

print("p_tuple element 1:",p_tuple[0])
print("p_tuple element 5:",p_tuple[4])

# 2.slicing tuple
print("\n* slicing tuple")

print("p_tuple:",p_tuple)
sliced_tuple = p_tuple[1:3]
print("sliced_tuple:",sliced_tuple)

# 4.deleting tuple
del sliced_tuple
del p_tuple
# use del tuple_name - to delete a tuple

# 5.modifying in tuple
# tuple is immutable which means we cannot change it after creation, but we can
# convert it into list then modify it and then again convert it into tuple
print("\n* # 5.modifying tuple")
p_tuple = ("python","java","cpp","perl")
print("tuple before:",p_tuple)
p_list = list(p_tuple)
p_list.append("javascript")
print("tuple converted to list:",p_list)
p_tuple = tuple(p_list)
print("list converted to tuple:",p_tuple)

# 6.adding tuple to a tuple
print("\n* # 5.adding tuple to a tuple")
n_tuple = ("english","science")
p_tuple += n_tuple
print("added p_tuple with n_tuple:",p_tuple)

# 7.unpacking tuple
# we initialize tuple we assign objects to it - this is known as packing a tuple
# extracting objects from tuple and assign them to variables is unpacking a tuple
print("\n* packing and unpacking tuple")

p_tuple = (1,2,3,4,5) # packing tuple
(one,two,three,four,five) = p_tuple # unpacking tuple
print("packed tuple:",p_tuple)
print("unpacked tuple:",one,two,three,four,five)

# Note:While unpacking a tuple, the number of variables on left-hand side should
# be equal to the number of elements in a given tuple. In case, the variables do
# not match the size of the tuple, we can use an asterisk '*'
# in order to store the remaining elements as a list.
print()
p_tuple = ("python","java","cpp","perl")
print("packed tuple:",p_tuple)
(python,java,*others) = p_tuple
print("python:",python)
print("java:",java)
print("others:",others)

# 8.looping tuples - same as lists

# 9.concatenating tuples
print("\n* concatenating tuples")
p_tuple = (1,2,3)
n_tuple = (4,5,6)
t_tuple = p_tuple + n_tuple

print("p_tuple:",p_tuple)
print("n_tuple:",n_tuple)
print("p_tuple + n_tuple:",t_tuple)

# 10.repetition tuples
print("\n* repetition tuples")
p_tuple = ("python","java")

print("p_tuple:",p_tuple)
print("p_tuple * 2:",p_tuple * 2)

# 11.membership
# using in,not in operators
p_tuple = ("python","java","cpp","perl")
print("\n* membership - in,not in")
print("p_tuple:",p_tuple)
if "javascript" not in p_tuple:
    print("javascript is not present")
if "java" in p_tuple:
    print("java is present")


# * Tuple Methods
# count() - use to count the occurrence of the specified element in a tuple
# index() - use to search for an element in the tuple and return its position
# max()
# min()
# len()
p_tuple = (1,2,4,5,1,2,8,7,6,5,1,1,7)
print("p_tuple:",p_tuple)
print("count of 1 in p_tuple:",p_tuple.count(1))
print("count of 5 in p_tuple:",p_tuple.count(10))
print("index of 8 in p_tuple:",p_tuple.index(8))

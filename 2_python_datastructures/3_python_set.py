# python set

# we create set using {} curly brackets
# set do not maintain the order of how elements are stored (it uses hash table)
# set is un-indexed which means we cannot access the data elements of sets
# each data item in set is unique
# set is mutable

# * operations on set
# 1.creation
# 2.adding element
# 3.removing element
# 4.union of set
# 5.intersection of set
# 6.difference of set
# 7.set comprehension

# 1.creation
print("* creating set")

p_set = {10,20,30,30,20,10}
print("p_set:",p_set)
m_set = {30,"hello",100,"world",2.55}
print("mixed_set:",m_set)

# 2.adding element
# - add(): This method is used to add a single element to the set
# - update(): This method is used to add multiple elements to the set
print("\n* adding element")

p_set = {'python','java'}
print("p_set:",p_set)
p_set.add('cpp')
print("added cpp p_set:",p_set)
p_set.update(['perl','javascript','php'])
print("added multiple items p_set:",p_set)

# 3.removing element
# - remove(): it is used to remove a specific element from the set
# it will raise a key-error if the element is not found in the set
# - discard(): it is used to remove a specified element from the set
# however, it does not raise any error if the element is not found
# - pop(): it is used to remove and returns a random element from the set
# - clear(): it is used to remove all the elements from the given set
print("\n* removing element")

print("p_set:",p_set)
p_set.remove("php")
print("removed php p_set:",p_set)
p_set.discard("javascript")
p_set.discard("cobol") # this is absent but will no throw error
print("p_set:",p_set)
p_set.pop()
print("removed random item p_set:",p_set)
p_set.clear()
print("removed all element p_set:",p_set)

# 4.union of set - A U B
# we can perform this using | operator and union() function
print("\n* union of set - A U B")

a_set = {1,2,3,4}
b_set = {2,3,5,6}
print("a_set:",a_set)
print("b_set:",b_set)
print("a_set | b_set:",a_set | b_set)
print("a_set.union(b_set):",a_set.union(b_set))

# 5.intersection of set - A ∩ B
# we can perform this using & operator and intersection() function
print("\n* intersection of set - A U B")

a_set = {1,2,3}
b_set = {2,3,5,6}
print("a_set:",a_set)
print("b_set:",b_set)
print("a_set & b_set:",a_set & b_set)
print("a_set.intersection(b_set):",a_set.intersection(b_set))

# 6.difference of set
# we can perform this using - operator and difference() function
print("\n* difference of set - A - B")

a_set = {1,2,3}
b_set = {2,3,5,6}
print("a_set:",a_set)
print("b_set:",b_set)
print("a_set - b_set:",a_set - b_set)
print("a_set.difference(b_set):",a_set.difference(b_set))

# 7.set comprehension
# it allows us to create sets in a concise and easy way
print("\n* set comprehension")

s_set = {i**2 for i in range(1,6)}
print("set of squares:",s_set)
c_set = {i**3 for i in range(1,6)}
print("set of cubes:",c_set)


# frozenset() - is immutable,unordered datatype it consist of unique items
# it is like normal set, but  it is immutable like tuple
print("\n* creating frozenset")

p_list = [10,20,30,30,20,10]
p_frozenset = frozenset(p_list)
print("p_list:", p_list)
print("p_list as frozenset:", p_frozenset)


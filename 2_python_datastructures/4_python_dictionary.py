# python dictionary

# dictionary store data in key value pairs
# it is mutable
# keys must be associated to one component or value
# value can be any type of object including list,integer,tuple

# operations on dictionary
# 1.creating dictionary
# 2.accessing values
# 3.adding/updating values
# 4.deleting values
# 5.iterating dictionary

# 1.creating dictionary
print("* creating dictionary")
language = {
    "name":"python",
    "founder":"guido van rossum",
    "founded":1991,
    "applications":["web development","machine learning","data science"]
}
print("type:",type(language))
print("language:",language)

# 2.accessing values
print("\n* accessing dictionary values")
print("language")
print("name: %s" %language["name"])
print("founder: %s" %language["founder"])
print("founded: %s" %language["founded"])
print("applications: %s" %language["applications"])

# 3.adding/updating values
print("\n* adding/updating dictionary values")

p_dict = {}
print("empty dictionary:", p_dict)
p_dict["name"] = "tony stark"
p_dict["alias"] = "iron man"
print("added values:",p_dict)

# Note: The value is updated if the key-value pair is already present
# in the dictionary. Otherwise, the dictionary's newly added keys.
p_dict["name"] = "peter parker"
p_dict["alias"] = "spider man"
print("updated values:",p_dict)

# creating dictionary with user input
# un-comment code to demonstrate
# print("\n* creating dictionary with user input")
# name = input("name: ")
# alias = input("alias: ")
# p_dict["name"] = name
# p_dict["alias"] = alias
# print("user input p_dict:",p_dict)

# 4.deleting values
print("\n* deleting values")

p_dict = {
    "l_1" : "python",
    "l_2" : "java",
    "l_3" : "cpp",
    "l_4" : "perl",
}
print("before deletion:")
print(p_dict)
del p_dict["l_4"]
print("deleted perl with key l_4")
print("p_dict:",p_dict)

# pop() is another way to remove dictionary item which will returns the value of
# deleted key
print("\n* deleting values using pop()")
print("before deletion")
print(p_dict)
value = p_dict.pop("l_2")
print("deleted value:",value)
print("after deletion:",p_dict)
# to delete whole dictionary we will use del p_dict

# 5.iterating dictionary
print("\n* iterating dictionary")
p_dict = {
    "l_1" : "python",
    "l_2" : "java",
    "l_3" : "cpp",
    "l_4" : "perl",
}
print("iterating on keys:",end=" ")
for i in p_dict:
    print(i,end=", ")
print()
print("iterating on values:",end=" ")
for i in p_dict:
    print(p_dict[i],end=", ")
print()
print("iterating on values using value():",end=" ")
for i in p_dict.values():
    print(i,end=", ")
print()
print("iterating on keys with values using items()")
for i in p_dict.items():
    print(i)


# properties of dictionary keys
# 1.we cannot store multiple values for the same keys. If we pass more than one
# value for a single key,then the value which is last assigned is considered
# as the value of the key

# 2. The key cannot belong to any mutable object in Python. Numbers, strings,
# or tuples can be used as the key, however mutable objects like lists cannot
# be used as the key in a dictionary.


# built-in dictionary functions
print("\n* built-in dictionary functions")
p_dict = {
    "l_1" : "python",
    "l_2" : "java",
    "l_3" : "cpp",
    "l_4" : "perl",
}

# len(p_dict) will return length of dictionary
print("len(p_dict):",len(p_dict))

# sorted(p_dict) to returns sorted series of dictionary keys
print("sorted(p_dict):",sorted(p_dict))

# p_dict.copy() returns a shallow copy of the dictionary which is created
n_dict = p_dict.copy()
print("n_dict:",n_dict)

# p_dict.clear() to delete all the items of dictionary
print("p_dict.clear():",p_dict.clear())

# n_dict.popitem() removes the most recent key-value pair entered
n_dict.popitem()
print("n_dict.popitem():",n_dict)

# n_dict.keys() returns all the keys of the dictionary
print("n_dict.key():",n_dict.keys())

# n_dict.values() returns all the values of the dictionary
print("n_dict.values():",n_dict.values())

# n_dict.items() returns all the items of the dictionary
print("n_dict.items():",n_dict.items())

# n_dict.get(key) used to get the value specified for the passed key
# if passed key is absent function will return none
print("n_dict.get(l_2):",n_dict.get("l_2"))

# n_dict.update({key:value}) updates all the dictionary by adding key-value pair
n_dict.update({"l_5":"js"})
print("n_dict.update({key:value}):",n_dict)

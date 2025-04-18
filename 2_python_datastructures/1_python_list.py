# * python list

# we create list using square brackets
# it is ordered which means list maintains the order of insertion
# list is mutable which means it allows modification after creation
# list is heterogeneous which me it can store elements of multiple data types

# * operations on list
# 1.creation
# 2.accessing element
# 3.adding element
# 4.updating element
# 5.removing element
# 6.iterating list

# 1.creation
empty_list = []
numbers = [1,2,4,5,2,1]
p_list = [1,"hello",2.5,"word",True]

print("* list creation")
print("empty list:",empty_list)
print("numbers:",numbers)
print("p_list:",p_list)

# 2.accessing elements
p_list = [1,"hello",2.5,"word",True]

print("\n* accessing list element")
print("item from number list:",numbers[2])
print("item from p_list:",p_list[len(p_list) - 2])

# 3.adding element
# we can add elements in list using functions like
# append(): Adds a single element to the end of the list
# insert(): Inserts an element at a specific index
# extend(): Adds multiple elements to the end of the list
print("\n* adding element")

p_list = [80,90]
print("empty list:",p_list)
p_list.append(100)
print("append(100):",p_list)
p_list.insert(1,85)
print("insert(1,85):",p_list)
p_list.extend([101,102,103])
print("extend([101,102,103]):",p_list)

# 4.updating element
print("\n* updating element")

print("before update:",p_list)
p_list[3] = 1
p_list[4] = 2
p_list[5] = 3
p_list[6] = 4
print("after update:",p_list)

# 5.removing element
# there are three methods to remove elements from list
# remove(value): Removes the first occurrence of the value
# pop(index): Removes the element at a specific index
# del statement: Deletes an element or the entire list

print("\n* deleting element")
print("before deletion:",p_list)
p_list.remove(80)
p_list.remove(85)
print("remove() 80,85 using:",p_list)
p_list.pop(0)
print("pop() element at index 0:",p_list)
del p_list
# print("del will delete whole list:",p_list)

# 5.iterating list
print("\n* using for loop")

p_list = [100,200,300,400,500]
print("- using range() and indexes")
for i in range(len(p_list)):
    print(p_list[i],end=" ")

print("\n- using list item")
for i in p_list:
    print(i,end=" ")
print()

print("\n* using while loop")
i = 0
while i < len(p_list):
    print(p_list[i], end=" ")
    i += 1
print()

# creating a nested list
print("\n* iterating over nested list")
p_list = [[2,4,3],[9,7,4],[0,8,1]]
for i in p_list:
    for j in i:
        print(j,end=" ")
    print()

print("\n* sorting list using sort()")
p_list = [90,234,5,1,56,34]
print("before sort:",p_list)
p_list.sort()
print("after sort:",p_list)

print("\n* reversing list using reverse()")
print("before reverse:",p_list)
p_list.reverse()
print("after reverse:",p_list)

print("\n* max min in list")
print("list:",p_list)
print("max:",max(p_list))
print("min:",min(p_list))

print("\n* summation of list using sum()")
print("list:",p_list)
print("sum of list:",sum(p_list))
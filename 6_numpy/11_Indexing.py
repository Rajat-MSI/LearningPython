import numpy as np

arr = np.array([1,2,3,4,5])
print("arr:", arr)
print("basic indexing")
print("arr[:3]- start to index (items before index 3):",arr[:3])
print("arr[2:]- index to end (items from index 2 to end):",arr[2:])
print("arr[1:4]- middle slice (items from index 1 to items before index 4):",arr[1:4])

print("\nnegative indexing")
print("arr[-3:]- last n elements (last n elements): ",arr[-3:])
print("arr[:-2]- all exepts last n elements: ",arr[-3:])
print("arr[4:1:-1]- negative step (starts at index 4, move backward to index 1): ",arr[-3:])

print("\nstepped slicing")
print("arr[::2]- every nth element (every second element):",arr[::2])
print("arr[::-1]- reverse array (reverse the entire array):",arr[::2])
print("arr[1:5:2]- stepped slice with range \n(starts at index 1 goes to 5"
      " taking every 2nd element):",arr[1:5:2])

print("\ncombination of integers and slice objects")
arr = np.arange(12).reshape(3,4)
print("original arr:", arr)
print("arr[1,2:4] value:", arr[1,2:4])


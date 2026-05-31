import numpy as np

# splitting into equal sized sub arrays axis=1 means cut horizontally
arr = np.arange(9).reshape(3,3)
arr_split = np.split(arr,3,axis=1)
print("original arr:", arr)
print("split arr:")
for sub_arr in arr_split:
    print(sub_arr)

print()

# splitting at specific indices [1 and 2] axis=0 means cut vertically
arr_split = np.split(arr,[1,2],axis=0)
print("original arr:", arr)
print("split arr:")
for sub_arr in arr_split:
    print(sub_arr)

print()

# splitting using array_split
arr = np.arange(10)
arr_split = np.array_split(arr,3,axis=0)
print("original arr:", arr)
print("split arr:", arr_split)

print()

# splitting using hsplit
arr = np.array([[1,2,3,4],[5,6,7,8]])
arr_split = np.hsplit(arr,2)
print("original arr:", arr)
print("horizontal split arr:", arr_split)

print()

# splitting using vsplit
arr_split = np.vsplit(arr,2)
print("original arr:", arr)
print("vertical split arr:", arr_split)

print()

# splitting using dsplit
arr = np.arange(24).reshape((2,3,4))
arr_split = np.dsplit(arr,2)
print("original arr:", arr)
print("vertical split arr:", arr_split)


import numpy as np

# using flatten
arr = np.array([[1,2,3],[4,5,6]])
arr_flatten = arr.flatten(order='C')
print("original arr:", arr)
print("flatten arr:", arr_flatten)

print()

# using ravel
arr = np.array([[1,2,3],[4,5,6]])
arr_ravel = arr.ravel(order='F')
print("original arr:", arr)
print("raveled arr view:", arr_ravel)
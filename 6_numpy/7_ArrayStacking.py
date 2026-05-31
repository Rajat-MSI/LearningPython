import numpy as np

# stacking 1D arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([7,8,9])
arr_stacked = np.stack((arr1,arr2,arr3),axis=0)
print("original arr1:",arr1)
print("original arr2:",arr2)
print("original arr3:",arr3)
print("array stacked:",arr_stacked)

print()

# stacking multidimensional arrays
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr_stacked = np.stack((arr1,arr2),axis=2)
print("original arr1:",arr1)
print("original arr2:",arr2)
print("array stacked:",arr_stacked)

print()

# column-wise stacking 1D arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr_stacked = np.column_stack((arr1,arr2))
print("original arr1:",arr1)
print("original arr2:",arr2)
print("array stacked:",arr_stacked)

print()

# column-wise stacking 2D arrays
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr_stacked = np.column_stack((arr1,arr2))
print("original arr1:",arr1)
print("original arr2:",arr2)
print("array stacked:",arr_stacked)

print()

# vertical stacking 2D arrays
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr_stacked = np.vstack((arr1,arr2))
print("original arr1:",arr1)
print("original arr2:",arr2)
print("array stacked:",arr_stacked)

print()

# horizontal stacking
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[7,8,9],[10,11,12]])
arr_stacked = np.hstack((arr1,arr2))
print("original arr1:",arr1)
print("original arr2:",arr2)
print("array stacked:",arr_stacked)

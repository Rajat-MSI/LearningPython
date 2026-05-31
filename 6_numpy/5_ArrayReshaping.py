import numpy as np

def output(arr1,arr2):
    print("original array:", arr1)
    print("original shape:", arr1.shape)
    print("reshaped array:", arr2)
    print("reshaped shape:", arr2.shape)

# reshaping 1D to 2D array
arr = np.array([1,2,3,4,5,6])
arr_reshape = arr.reshape(2,3)
output(arr,arr_reshape)

print()

# reshaping 1D to 3D array
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr_reshape = arr.reshape(2,2,3)
output(arr,arr_reshape)

print()

# reshaping ND to 1D array
arr = np.array([[1,2,3],[2,3,4]])
arr_reshape = arr.reshape(-1)
output(arr,arr_reshape)

print()

# reshaping to unknown dimension
arr = np.array([1,2,3,4,5,6,7,8])
arr_reshape = arr.reshape(2,2,-1)
output(arr,arr_reshape)
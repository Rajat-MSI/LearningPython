import numpy as np

# transposing 2D array
arr = np.array([[1,2,3],[4,5,6]])
arr_transposed = np.transpose(arr)
print("original arr:", arr)
print("transposed arr:", arr_transposed)

print()

# transposing 3D array
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr_transposed = np.transpose(arr)
print("original arr:", arr)
print("transposed arr:", arr_transposed)

print()

# transposing with specified axes
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr_transposed = np.transpose(arr,axes=(0,2,1))
print("original arr:", arr)
print("transposed arr:", arr_transposed)


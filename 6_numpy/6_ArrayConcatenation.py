import numpy as np

# concatenating arrays along rows
arr1 = np.array([[1,2,3],[4,5,6]])
arr2 = np.array([[0,9,8],[1,2,3]])
arr_concatenated = np.concatenate((arr1,arr2),axis=0)
print("original arrays:",arr1,"\n",arr2)
print("concatenated along rows:",arr_concatenated)

print()

# concatenating arrays along columns
arr_concatenated = np.concatenate((arr1,arr2),axis=1)
print("original arrays:",arr1,"\n",arr2)
print("concatenated along columns:",arr_concatenated)

print()

# concatenating arrays with mixed dimensions
arr1 = np.array([1,2,3])
arr2 = np.array([[4,5,6],[7,8,9]])
arr_expanded = np.expand_dims(arr1, axis=0)
arr_concatenated = np.concatenate((arr_expanded,arr2),axis=0)
print("original arrays:",arr1,"\n",arr2)
print("array 1 expanded:",arr_expanded)
print("concatenated along rows:",arr_concatenated)

print()

# concatenating 2D array with 3D array
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
arr_expanded = np.expand_dims(arr1,axis=2)
arr_concatenated = np.concatenate((arr_expanded,arr2),axis=2)
print("original arrays:",arr1,"\n",arr2)
print("array 1 expanded:",arr_expanded)
print("concatenated along rows:",arr_concatenated)





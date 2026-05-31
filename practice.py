import numpy as np

arr1 = np.array([[[1,2,3],[4,5,6]]])
arr2 = np.array([[[4,5,6],[7,8,9]]])
arr_expanded = np.expand_dims(arr1, axis=0)
arr_concatenated = np.concatenate((arr1,arr2),axis=0)
print("original arrays:",arr1,"\n",arr2)
print("array 1 expanded:",arr_expanded)
print("concatenated along rows:",arr_concatenated)


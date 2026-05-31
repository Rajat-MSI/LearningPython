import numpy as np

print("using astype() function")
arr = np.array([1,2,3,4,5])
print("array as integer:", arr)
print("original dtype:", arr.dtype)

arr_float32 = arr.astype(np.float32)
print("array as float:", arr_float32)
print("converted dtype:", arr_float32.dtype)

print("\nusing numpy.cast")
arr_int = np.int8(arr_float32)
print("array as int8:",arr)
print("converted dtype:", arr_int.dtype)

arr_inplace = np.array([10,20,30], dtype=float)
print("array converted in-place: ",arr_inplace)









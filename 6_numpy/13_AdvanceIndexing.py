# integer indices
# selecting elements by indices [x,y,z] position
import numpy as np

arr = np.array([[1,2],[3,4],[5,6]])
arr_cord = arr[[0,1,2],[0,1,0]]
print("original arr:",arr)
print("new arr from indices:",arr_cord)

print()

# selecting corner elements
arr = np.array([[0,1,2],[3,4,5],[6,7,8],[9,10,11]])
arr_rows = np.array([[0,0],[3,3]])
arr_cols = np.array([[0,2],[0,2]])
arr_res = arr[arr_rows,arr_cols]
print("result:", arr_res)

print()

# boolean indices
arr = np.arange(10,60,10)
arr_bool = np.array([True,False,True,False,True])
arr_res = arr[arr_bool]
print("original arr:", arr)
print("bool arr:", arr_bool)
print("res arr:", arr_res)

print()

# extracting even numbers
arr = np.arange(1,11)
print("even numbers:",arr[arr % 2 == 0])
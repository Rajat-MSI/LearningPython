import numpy as np

# slicing in 1D arrays
print("slicing in 1D arrays")
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print("arr[1:8:2] value:",arr[1:8:2])

print()

# slicing with start parameter
print("slicing with start parameter")
print("arr[2:] value:",arr[2:])

print()

# slicing with end parameter
print("slicing with end parameter")
print("arr[:7] value:",arr[:7])

print()

# slicing in 2D arrays
print("slicing in 2D arrays")
arr = np.array([
    [1, 25, 50000],
    [2, 30, 60000],
    [3, 28, 55000],
    [4, 35, 65000],
    [5, 40, 70000]
])
print("arr[2:,1] value:",arr[2:,1])

print()

# slicing in 3D arrays
print("slicing in 3D arrays")
arr = np.arange(24).reshape(2,3,4)
print("original arr:",arr)
print("arr[0, :, :2] value:",arr[0,:,:2])

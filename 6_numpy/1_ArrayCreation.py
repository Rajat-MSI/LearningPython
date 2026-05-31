import numpy as np

p_list = [1,2,3,4,5]
arr = np.array(p_list)
print("p_list:", p_list," type:", type(p_list))
print("arr:", arr," type:", arr.dtype)

print("\n")

arr = np.zeros(5)
print("arr:", arr)
print("arr:", arr," type:", arr.dtype)

print("\n")

arr = np.ones((3,3), dtype=int, order='C')
print("arr:", arr)
print("type:", arr.dtype)

print("\n")

arr = np.arange(3,30,3)
print("arr:", arr)
print("type:", arr.dtype)


print("\n")

arr, step = np.linspace(1, 5, 10, endpoint=True, retstep=True)
print("arr:", arr)
print("step size:", step)
print("type:", arr.dtype)

print("\n")

arr = np.random.rand(2,3)
print("arr:", arr)
print("type:", arr.dtype)

print("\n")

arr = np.empty((2,3))
print("arr:", arr)
print("type:", arr.dtype)

print("\n")

arr = np.full((2,3),5)
print("arr:", arr)
print("type:", arr.dtype)
import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
for i in arr:
    print(i,end=' ')

print("\n")

arr = np.arange(1,10).reshape(3,3)
for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        print(arr[i,j],end=' ')
    print()
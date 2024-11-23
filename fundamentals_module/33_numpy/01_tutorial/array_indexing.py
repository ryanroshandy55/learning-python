# NumPy array indexing is start from 0 and the next index is 1
# it's was same with structure data for array that not started from 1, but it's started from 0

# Array indexing is the same as accessing an array element

import numpy as np

arr = np.array([1, 2, 3, 4])

print(arr[0])
print(arr[1])
print(arr[2] + arr[3])

print("------------------")

arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])

print(arr)

print('2nd element on 1st row: ', arr[0, 1])
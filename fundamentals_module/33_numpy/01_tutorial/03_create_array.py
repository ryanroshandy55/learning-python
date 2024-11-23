import numpy as np

arr = np.array([1,2,3,4,5])

print(arr)
print(type(arr), "\n")



arr = np.array((1,2,3,4,5))

print(arr)
print(type(arr), "\n")

# Array dimension 
# 0D Arrays
arr_0d = np.array(42)
print("array 0-D :", arr_0d)


# 1D Array
arr_1d = np.array([1,2,3,4,5])
print("array 1-D :", arr_1d)


# 2D Array
arr_2d = np.array([[1,2,3], [4,5,6]])
print("array 2-D :\n", arr_2d)


# 3D Array
arr_3d = np.array([[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]])
print("array 3-D :\n", arr_3d)
print(arr_3d.ndim)
print("-----------------")


# 4D Array
arr_4d = np.array([[[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]], [[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]]])
print("array 4-D :\n", arr_4d)
print(arr_4d.ndim)
print("-----------------")

# 5D Array (I'm just trying and wanted to know)
arr_5d = np.array([[[[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]], [[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]]], [[[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]], [[[1,2,3], [4,5,6]], [[1,2,3], [4,5,6]]]]])
print("array 5-D :\n", arr_5d)
print(arr_5d.ndim)
print("-----------------")

# More dimension it's will more confusing and complex

# Vreate an array with 5 dimensions and verify that it has 5 dimensions
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)
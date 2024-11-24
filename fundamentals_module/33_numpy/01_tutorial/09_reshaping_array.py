# Reshaping arrays
# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

import numpy as np

# Reshape from 1-D to 2-D
# Example
# Convert the following 1-D array with 12 elements into a 2-D array.
# The outermost dimension will have 4 arrays, each with 3 elements:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
print(arr)

newarr = arr.reshape(4, 3)    # reshape(array, elements)
print(newarr)

print("\n-------------------------------")
# Reshape from 1-D to 3-D
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)    # reshape (array, containts_array, elements)
print(newarr)

print("\n-------------------------------")


# Can we reshape into any shape?
# Yes, as long as the elements required for reshaping are equal in both shapes.
# We can reshape an 8 elements 1D array into 4 elements in 2 rows 2D array
# but we cannot reshape it into a 3 elements 3 rows 2D array
# as that would require 3x3 = 9 elements.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
# newarr = arr.reshape(3,3) # raise an error
newarr = arr.reshape(4, 2)

print(newarr)

print("\n-------------------------------")
# Return copy or view
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

print(arr.reshape(2, 4).base)

print("\n-------------------------------")

# Unknown Dimension
# You are allowed to have one "unknown" dimension
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method
# Pass -1 as the value, and NumPy woll calculate this number for you
# Example
# Convert 1D array with 8 elements to 3D array with 2x2 elements:

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
new = arr.reshape(2, 2, -1)
print(newarr)


# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array
# We can use reshape(-1) to do this.
# Example
# Convert the array into a 1D array:

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)

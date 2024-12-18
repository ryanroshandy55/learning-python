# Shape of an array
# Print the shape of a 2-D array

import numpy as np

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr.shape)

# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4
arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('Shape of array :', arr.shape)

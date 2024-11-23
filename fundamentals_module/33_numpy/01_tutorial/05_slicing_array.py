import numpy as np

arr = np.array([1,2,3,4,5,6,7])

print(arr[1:5])

# Slice element from index 4 to end of the array
print(arr[4:])


# Slice elements from the beginning to index 4 (not included index 4 or arr[3])
# note : indexing in numpy array start from 0 .. so the index_num = array[index]+1

print(arr[:4])

# Negative Slicing
arr = arr

print(arr[-3:-1])


# STEP
# Use the step value to determine the step of slicing
# Return every other element from index 1 to index 5
arr = np.array([1,2,3,4,5,6,7])

print(arr[1:5:2])


# Return every other element from the entire array
print(arr[::2])


# Slicing 2-D Arrays
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1, 1:4])


# from both elements, return index 2
print(arr[0:2, 2])

# From both elements, slice index 1 to index 4 (not included), this will return a 2-D array
print(arr[0:2, 1:4])
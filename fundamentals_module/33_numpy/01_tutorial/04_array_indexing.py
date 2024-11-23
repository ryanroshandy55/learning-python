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

# Access 2D Arrays
# To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.
# Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.

# Access the element on the first row, second column:
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])


# Accest the element on the 2nd row, 5th column
import numpy as np

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('5th element on 2nd row: ', arr[1, 4])

# Access 3-D Arrays
# To access elements from 3-D arrays we can use comma separated integers representing the dimensions and the index of the element.

import numpy as np

arr = np.array([[[1,2,3],[4,5,6]],[7,8,9],[10,11,12]])

print(arr[0,1,2])


# Negative indexing
# Use negative indexing to access an array from the end

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print("Last element from 2nd dim: ", arr[1, -1])
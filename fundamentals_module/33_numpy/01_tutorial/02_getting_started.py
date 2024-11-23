import numpy

# if you do not have numpy library in your computer, download it first
# pip install numpy

arr = numpy.array(["a","b","c","d","e"])

# This is for making numpy shorten, do it as alias np (general alias)
import numpy as np

arr_np = np.array([1,2,3,4,5])  # -> define np array

print(arr, arr_np)      # -> print output

# if you want to see numpy version, we can print this
print(np.__version__)
# my numpy version is 2.1.3 when i write this code
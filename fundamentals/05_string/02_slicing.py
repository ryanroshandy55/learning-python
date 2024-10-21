# slicing is for return a range of characters by using the slice syntax
'''specify the start index and the end index, separate by semicolon
to return part of the string'''

# remember arrays start with [0]
# slicing from string array position 2 to 5 (not included)
# [2][3][4] llo
b = "Hello, World!"
print(b[2:5])

# slicing from start
# start from [0] to 5 (not included)
# [0][1][2][3][4] Hello
b = "Hello, World!"
print(b[:5])

# slicing to the end
# slicing from string array position x to end
b = "Hello, World!"
print(b[2:])

# negative indexing
b = "Hello, World!"
print(b[-5:-2])
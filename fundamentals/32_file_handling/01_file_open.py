# File Handling
# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:
    # "r" - Read - Default value. Opens a file for reading, error if the file does not exist
    # "a" - Append - Opens a file for appending, creates the file if it does not exist
    # "w" - Write - Opens a file for writing, creates the file if it does not exist
    # "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode
    # "t" - Text - Default value. Text mode
    # "b" - Binary - Binary mode (e.g. images)

# syntax
# f = open("demofile.txt")

# f = open("demofile.txt", "rt")

# Make sure the file is exist

# without r and with r
f = open("fundamentals\\32_file_handling\\demofile.txt")
f = open(r"fundamentals\32_file_handling\demofile.txt")
f = open("fundamentals/32_file_handling/demofile.txt")

print(f.read(), "\n")

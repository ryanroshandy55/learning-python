# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:
#     "a" - Append - will append to the end of the file
#     "w" - Write - will overwrite any existing content

# ExampleGet your own Python Server
# Open the file "demofile2.txt" and append content to the file:

# Template text
# Hello! Welcome to demofile.txt
# This file is for testing purposes.
# Good Luck!

f = open("fundamentals/32_file_handling/demofile2.txt", "w")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("fundamentals/32_file_handling/demofile2.txt", "r")
print(f.read())

f = open("demofile3.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("demofile3.txt", "r")
print(f.read())


# Create a New File
# To create a new file in Python, use the open() method, with one of the following parameters:
    # "x" - Create - will create a file, returns an error if the file exists
    # "a" - Append - will create a file if the specified file does not exists
    # "w" - Write - will create a file if the specified file does not exists

f = open("fundamentals/32_file_handling/myfile.txt", "x")

f = open("fundamentals/32_file_handling/myfile.txt", "w")
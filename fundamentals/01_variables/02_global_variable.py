# This define x with string values "awesome"
x = "awesome"

# Function to call x
def myFunc():
    print("Python is " + x)

# Call function from global variable (x)
myFunc()
###################
# Output:
# Python is awesome
###################


# Custom above
x = "awesome"

# Function to call x but here we get
def myFunc():
    x = "Fantastic"
    print("Python is " + x)

# Call function from global variable (x)
myFunc()
print("Python is " + x)
######################
# Output:
# Python is Fantastic
# Python is awesome
######################


# Well we try to set x in function to be global variable
def myfunc():
    global x
    x = "great"

# X only will be global if we call func first
myfunc()
print("Python is " + x)
######################
# Output:
# Python is great
######################


# Well we try to set x in function to be global variable
def myfunc():
    global x
    x = "great"

# X only will be global if we call func first
myfunc()
print("Python is " + x)
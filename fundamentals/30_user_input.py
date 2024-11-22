# User input
# This code is used to input and can used for defined a variable

# This is for python 3.6 and latest
username = input("Enter username:")
print("Username is: " + username)

# This is for python 2.7 (raw_input()) cannot used in python 3.6 and latest
try:
    username = raw_input("Enter username:")
    print("Username is: " + username)
except: 
    print("This raw_input cannot used")
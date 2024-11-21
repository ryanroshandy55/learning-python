# Local Scope
def myfunc():
    x = 300
    print(x)
    
myfunc()

print("========")


# Function inside function
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

print("========")


# Global Scope
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.

# Global variables are available from within any scope, global and local.

x = 300

def myfunc():
    print(x)
    
myfunc()

print(x)

print("========")


# Naming variables
x = 300

def myfunc():
    x = 200
    print(x)
    
myfunc()

print(x)

print("========")


# Nonlocal keyword
def myfunc1():
    x = "Jane"
    def myfunc2():
        nonlocal x
        x = "hello"
    myfunc2()
    return x

print(myfunc1())
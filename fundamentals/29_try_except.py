# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# The else block lets you execute code when there is no error.
# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Basic of try and except this used for error handling, 
# in some case this code used for testing the program.

# try and except basic
print("Try and Except basic")
try:
    print(x)
except:
    print("There is something error")


print("===========")


print("except with some specific or raises error (NameError)")
# Many exceptions
try:
    print(x)
except NameError:
    print("Variable is not defined")
except:
    print("An exception occured")
    print("Something else went wrong")

print("===========")


print("else example code when nothing wrong")
# Else that can be output when the code has no error
try:
    print("Hello")
except:
    print("An exception occured")
    print("Something else went wrong")
else:
    print("Nothing went wrong")

print("===========")


print("Finally example") 
# Finally
# The finally block, if specified, will be  excuted regardless if the try block raises an error or not.
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")
    
# This can be useful to close objects and clean up resources

try:
    f = open("demofile.txt")
    try:
        f.write("Lorem Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


print("===========")

print("Raise an exception example") 
# Raise an exception
# As a Python developer you can choose to throw an exception if a condition occurs.

# To throw (or raise) an exception, use the raise keyword.
x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

print("===========")

x = "hello"

if not type(x) is int:
    raise TypeError("Only integers are allowed")
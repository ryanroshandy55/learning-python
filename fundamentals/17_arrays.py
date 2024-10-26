# Python arrays
# Arrarys

# Note: This page shows you how to use LISTS as ARRAYS, however, to work with arrays in Python you will have to import a library, like the NumPy library.
# Arrays are used to store multiple values in one single variable:

# Example
# Get your own Python Server
# Create an array containing car names:

cars = ["Ford", "Volvo", "BMW"]

car1 = "Ford"
car2 = "Volvo"
car3 = "BMW"

cars[0] = "Toyota"

x = cars[0]
print(x)
print(cars)

x = len(cars)
print(x)

# Looping array elements
# You can use the for in loop to loop through all the elements of an array

# example
# print each item in the cars array
for x in cars:
    print(x)

cars.append("Honda")
print(cars)

# Removing array elements
# You can use the pop() method to remove an element from the array
cars.pop(1)
print(cars)

# You can also use the remove() method to remove an elemenet from the array
cars.remove("Volvo")


# Array Methods
# Python has a set of built-in methods that you can use on lists/arrays.

# Method	    Description
# append()	    Adds an element at the end of the list
# clear()	    Removes all the elements from the list
# copy()	    Returns a copy of the list
# count()	    Returns the number of elements with the specified value
# extend()	    Add the elements of a list (or any iterable), to the end of the current list
# index()	    Returns the index of the first element with the specified value
# insert()	    Adds an element at the specified position
# pop()	        Removes the element at the specified position
# remove()	    Removes the first item with the specified value
# reverse()	    Reverses the order of the list
# sort()	    Sorts the list
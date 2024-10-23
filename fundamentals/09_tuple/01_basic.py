# Tuple 
# Tuple are used to store multiple items in a single variable
# Tuple is one of built-in data types in Python to store collections of data

thistuple = ("Apple", "Banana", "Cherry")
print(thistuple)

# Tuple item is
# Ordered = tuple have defined order and that order will not change
# Unchangeable = tuple cannot change, add, or remove items after the tuple has been created
# Allow duplicates = tuple are indexed and can have same value

thistuple = ("Apple", "Banana", "Cherry", "Apple", "Cherry")
print(thistuple)

# AttributeError: 'tuple' object has no attribute 'insert'
# thistuple.insert(0, "Pear") 

# AttributeError: 'tuple' object has no attribute 'clear'
# thistuple.clear()


# Tuple Length

print(len(thistuple))

# THIS a tuple
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

print(tuple1)
print(tuple2)
print(tuple3)

# the tuple() costructor
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)
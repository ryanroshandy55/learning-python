myset = {"apple", "banana", "cherry"}
print(myset)
print(type(myset))

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.

# Unordered
# Unordered means that the items in a set do not have a defined order.

# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

# Unchangeable
# Set items are unchangeable, meaning that we cannot change the items after the set has been created.

# Duplicates not allowed
# The code will run but the dupe value will only show the first value and other will ignored
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)

# the True value and 1 is considered as the same value in sets
# and threatened as duplicates
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

# the False value and 0 is considered as the same value in sets
# and threatened as duplicates
thisset = {"apple", "banana", "cherry", False, True, 0, 1, 2}

print(thisset)


# Get the Length of a Set
print(len(thisset))


# Sets data types
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# Sets type
myset = {"apple", "banana", "cherry"}
print(type(myset))

# the set() constructor
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
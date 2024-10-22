# List
# List are used to store multiple items items in a single variable
thislist = ["app", "win", "mac", "lin"]
print(thislist)


# Allow duplicates
thislist = ["app", "mac", "win", "mac", "lin"]
print(thislist)
print(len(thislist))


# List Items - Data Types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1, list2, list3)

# Containts data types combination
list1 = ["abc", 34, True, 40, "male"]
print(list1)

print(type(list1))

# The list() constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Python collections (arrays)
# list      - is a collection which is ordered and changeable. Allows duplicate members
# tuple     - is a collection which is ordered and unchageable. Allows duplicate members
# set       - is a collection whics is unordered, unchangeable*, and unindexed. no duplicate members.
# dictionary- is a collection which is ordered** and changeable. No duplicate members

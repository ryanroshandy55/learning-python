# Join sets
# There are several ways to join two or more sets in Python
# The union() and update() methods joinss all items from both sets
# The intersection() method keeps ONLY the duplicates
# The difference() method keeps the items ffrom the first set that are not in the other set(s)
# The symmetric_difference() method keeps all items EXCEPT the duplicates

# Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

for x in range (5):
    set3 = set2.union(set1)
    print(set3)

# Can use operator `|` instead of union(), and get same result
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)


# Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)


# When using the | operator, separate the sets with more | operators:
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)

# Join sets and a tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

# Update
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

# Intersection
# Keep ONLY the duplicates

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)

# Use & operator instead intersetion()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)

# The intesection_update() method will also keep ONLY the duplicates
# and keep the change on the original set instead of returning a new set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

# The values True and 1 are considered the same value. The same goes for False and 0
set1 = {"apple", 1, "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)

# Difference
# The difference() method will return a new set that will contain only the items from the first set
# that are not present in the other set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

# Using operator - instead difference()
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)

# sets difference_update() method to keep the items that are not present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)

# Symmetric Differences
# The symetric_difference() method will keep only the element that are NOT present in both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)

# You can use operator ^, this operator have same function with symmetric_difference() method
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
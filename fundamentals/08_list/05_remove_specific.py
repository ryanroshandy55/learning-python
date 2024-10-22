# Remove specified item
# Remove()
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# Remove the first occurence of "banana"
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove specified index
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

# Remove not specified, but last item in the list
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# del also can delete entire list completely
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the list
# using clear() method to empty the list
# but list still remain, but empty
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
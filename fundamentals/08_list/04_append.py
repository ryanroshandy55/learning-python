# Append
# is used to add item in the end of the list
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

# To insert a list of item in specific index is need to use insert(position, "value") || insert(position, value)
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

# Extend list
# to append elements from another list to the current list
# use the extend() method
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)


# Add any iterable
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
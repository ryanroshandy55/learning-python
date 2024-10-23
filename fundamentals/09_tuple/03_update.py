# Change tuple values
# Once tuple is created. you cannot change it value
# but there is some work around with it,
# you can convert the tuple into a list, 
# change the list, and convert the list back into a tuple
x = ("apple", "banana", "cherry")
y = list(x)

y[1] = "kiwi"
x = tuple(y)

print(x)

# This procedure is kind of changing variable type to change tuple value


# for adding item is the same of technique from above
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")

thistuple = tuple(y)


# make tuple > make variable that convert tuple to list > append > the second change to tuple again 
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# remove items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# del keyword to delete the tuple completely
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
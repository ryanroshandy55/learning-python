# Removing items
# The pop() method removes the item with the specified key name
thisdict = {
    "brand": "BMW",
    "model": "M6",
    "year": 2018
}
thisdict.pop("model")
print(thisdict)

# the popitem() method removes the last inserted item (in versions before 3.7
# , a random item is removed instead)
thisdict = {
    "brand": "BMW",
    "model": "M6",
    "year": 2018
}
del thisdict["model"]
print(thisdict)

# del dictionary completely
thisdict = {
    "brand": "BMW",
    "model": "M6",
    "year": 2018
}
del thisdict
# print(thisdict) # this will cause an error because "thisdict" no longer exist

# the clear() method empties the dictionary
thisdict = {
    "brand": "BMW",
    "model": "M6",
    "year": 2018
}
thisdict.clear()
print(thisdict)
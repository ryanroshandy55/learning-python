# This is dictionaries
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Dictionary Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# Duplicates NOT Allowed
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisdict)

# Check dictionary len
print(len(thisdict))

# Data types of dictionary item
# dictionary can containts String, int, boolean, and list data types
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}

# type()
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(type(thisdict))

# The dict() Constructor
# It is also possible to use the dict() constructor to make a dictionary
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)
# Accessing items in dictionary
# Dictionary concept
# variable = {"n_key": "n_value"}

# Get the value of the "model" key
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]

# There is also a method called get() that will give you the same result:
x = thisdict.get("model")
print(x)

# Get a list of the keys:
x = thisdict.keys()
print(x)

# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x) #before the change

car["color"] = "white"
print(x) #after the change

# Get Values
# The values() method will return a list of all the values in the dictionary
x = thisdict.values()
print(x)

# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()
print(x, "= before change") #before the change

car["year"] = 2020
print(x, "= after change") #after the change

# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
# Get a list of the key:value pairs
x = thisdict.items()
print(x)

# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
# Example
# Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x) #before the change

car["year"] = 2020
print(x) #after the change

# Add a new item to the original dictionary, and see that the items list gets updated as well:

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.items()
print(x) #before the change

car["color"] = "red"
print(x) #after the change

# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
# Example
# Check if "model" is present in the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
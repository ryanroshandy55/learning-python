# change value
# You can change the value of a specific item by referring to its key name:
# Change the "year" to YYYY
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}
thisdict["year"] = 2024
print(thisdict)


# update dictionary
# the update() method will update the dictionary with the items from the given argument
# the argument must be a dictionary, or an iterable object with key:value pairs
# update the "year" of the car by using the update() method:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
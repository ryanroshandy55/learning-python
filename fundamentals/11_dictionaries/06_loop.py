# loop through a dictionary
# when looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well
thisdict = {
    "brand": "Audi",
    "model": "R8",
    "year": 2018
}
for x in thisdict:
    print(thisdict[x])

# Return dictionary loop values
for x in thisdict.values():
    print(x)

# Return dictionary loop from keys
for x in thisdict.keys():
    print(x)

# Loop through both keys and values, by using the item() method
# single variable loop
for x in thisdict.items():
    print(x)

# Loop through both keys and values, by using the item() method
# with 2 variable loop
for x, y in thisdict.items():
    print(x, y)
# Copy a dictionary
# dictionary cannot copied by simple using dict1 = dict2
# because the dict2 will only be a reference to dict1, and changes made in dict1
# will automatically also be made in dict2

# there are ways to make a copy, one way is to use the built-in dictionary method copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# another way to make a copy is to use the built-in function dict()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# Change item value
# to change the value of a specific item, refer to the index number:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a range of item values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)


# Insert items into list
thislist = ["apple", "banana", "cherry"]
thislist.insert(0, "watermelon")    # insert(position, value)
print(thislist)
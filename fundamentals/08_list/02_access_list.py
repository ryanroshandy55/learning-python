# Access List
# The list can access specific item using list[]
# Basic selection list arrays
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# This list is counted from the last
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# This list is start from 2 and stop on 5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# This list is start and stop on list num 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# This list is start from 2 till end
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# This list is start from "orange" (-4) to, but NOT including "mango"
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

# Check if item exist in the list
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
else:
    print("No, 'apple' is in the fruits list")
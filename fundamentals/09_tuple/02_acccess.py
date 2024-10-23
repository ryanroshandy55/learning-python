# Access tuple items by reffering/selection the index number
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Negative Indexing
# Negative indexing means start from the end
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])

# Range of indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Stop in the tuple number 4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

# Start index from number 2
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Range of Negative Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# Check if item Exist
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
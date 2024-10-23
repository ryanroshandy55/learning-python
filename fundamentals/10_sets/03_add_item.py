# Update Sets
# Update can use add() method
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")
print(thisset)

# Add sets
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)
print(thisset)

# Add any iterable object using update() methods
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)
print(thisset)
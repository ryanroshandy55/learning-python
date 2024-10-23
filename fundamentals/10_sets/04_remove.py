# Remove item
# Remove item can use remove() methods
# This example for removing banana from sets
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

# we can used discard() method, this method can avoid error if the set NOT EXIST
thisset = {"apple", "banana", "cherry"}
thisset.discard("banna")
print(thisset)

# use pop() method to remove random item
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
print(thisset)

# to empty set we can use clear() methods,
testa = set(thisset)
testa.clear()
thisset.clear()
print(testa)
print(thisset)

# this method will raise an error, because the sets have been remove entirely
del thisset
print(thisset)
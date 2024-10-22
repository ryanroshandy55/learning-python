# Loop through the list items by using a for loop
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
    
# Loop through the index numbers
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Using while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# Using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
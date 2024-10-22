# Sort list alphanumerically
# list object have a sort() method that will sort the list alphanumerically
# ascending, by default
thislist = ["orange", "mango", "kiwi", "pineaple", "banana"]
thislist.sort()
print(thislist)

# sort list numerical
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sort by descending categorical
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# Sort by descending numerical
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# Customize sort function
# You  also customize your own function by using the keyword argument key = function
# the function will return a number that will be used to sort the list (the lowest number first)
def myfunc(n):
    return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case insensitive sort
# result the capital will sort first 
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# Luckily we can use built-in functions as key functions when sorting a list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# Reverse order
# what if you wan to reserve the order of a list, regardless of the alphabet
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# This example code using for loop
# without comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# With list comprehension we can do that only one line single code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]
print(newlist)

# The Syntax
# newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [ x for x in fruits if x == "apple"]
print(newlist)

# without if statement
newlist = [x for x in fruits]
print(newlist)

# Iterable
# The iterable can be any iterable object, like a list, tuple, set etc
newlist = [x for x in range(10)]
print(newlist)

# same example, but with a condition
newlist = [x for x in range(10) if x < 5]
print(newlist)

# Expression
# The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before
# it ends up like a list item in the new list
newlist = [x.upper() for x in fruits]
print(newlist)

newlist = ['hello' for x in fruits]
print(newlist)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome
newlist = [x if x !="pear" else "orange" for x in fruits]
print(newlist)
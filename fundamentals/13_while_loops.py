# Python Loops
# python has two primitive loop commands
    # while loops
    # for loops

# The while loops
print("While")
i = 1
while i < 6:
    print(i)
    i += 1

# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.

# The break Statement
# With the break statement we can stop the loop even if the while condition is true:
print("Break")
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# The continue statement
# With the continue statement we can stop the current iteration, and continue with the next:
print("Continue")
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# The else Statement
print("Else Statement")
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
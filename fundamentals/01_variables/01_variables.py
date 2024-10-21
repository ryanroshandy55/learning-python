##################
# how to create variable in python
# String
x = "Hello"

y = 5       # automate int
ya = int(5)  # defined with int

z = 2.6     # automate float
za = float(2.6)

# Call the variables (output variables)
print(x)
print(type(y))
print((z))

# We can do substraction too or any simple operator
print(15 + 24)
print("y - z =", y - z)

########################
# Assign multiple variable
# Many values to multiple variables
x,y,z = "Orange", "Banana", "Cherry"
print(x , y, z)

# Many variable with same value
x = y = z = "Banana"
print(x, y, z)

# using List, this how we unpack a list
fruits = ["Orange", "Banana", "Cherry"]
x, y, z = fruits
print(type(fruits))
print(x,y,z)
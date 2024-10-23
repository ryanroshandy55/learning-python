# Unpacking a Tuple
# this is packing a tuple
fruits = ("apple", "banana", "cherry")

# this is how to unpacking the tuple
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# Using asterisk*
# If the number of variables is less than the number of values, 
# you can add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)


# This method can used in the middle variable, it will make red jump to the last tuple
# and the asterisk tuple containts entire value that not have variable
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)
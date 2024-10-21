# substraction the string with variable define with number
# will return error, we can change the format to str for avoid error
# it will be an error
age = 36
# txt = "My name is John, I am " + age  # Error
txt = "My name is John, I am " + str(age) 
print(txt)


# f-string is for input variable in string
age = 36
txt = f"My age is {age}"
print(txt)

# placeholders and modifiers can contain variables, operations
# functions and modifiers to format the value
price = 59
txt = f"The price is {price} dollars"
print(txt)

# Display price with 2 decimals
price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# perform a math operation in the placeholder, and return all result
txt = f"The price is {20 * 59} dollars"
print(txt)
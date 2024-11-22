# Python string formatting
# F- String was introduced in Python 3.6, and is now the preffered way of formatting strings
# Before python 3.6 we had to use the format() method

# Bellow 3.6 version first, string formatting example
print("==========================================")
print("3.6 and Below version string formatting")
print("==========================================")
print("-------------------------------")
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))

txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
txt2 = "My name is {0}, I'm {1}".format("John",36)
txt3 = "My name is {}, I'm {}".format("John",36)

quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(quantity, itemno, price))


quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))


age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))

# 3.6 and above version string formatting
print("==========================================")
print("3.6 and above version string formatting")
print("==========================================")

txt = f"The price is 49 dollar"
print(txt)

print("-------------------------------")

# Place holders and modifiers

price = 59
txt = f"The price is {price} dollars"
print(txt)


# Display the price with 2 decimals
price = 59
txt = f"The price is {price:.2f} dollars // with 2 decimals"
print(txt)

txt = f"The price is {95:.2f} dollars // display value 95 with 2 decimals"
print(txt)

txt = f"The price is {20 * 59} dollars // perform operations in F-strings (20 * 59)"
print(txt)

price = 59
tax = 0.25
txt = f"The price is {price + (price * tax)} dollars // perform operation math variables price + (price * tax) "
print(txt)


# Execute functions in F-strings
fruit = 'apples'
txt = f"I love {fruit.upper()}"
print(txt)

# Create a function tha converts feet into meters:
def myconverter(x):
    return x * 0.3048

txt = f"The plane is flying at a {myconverter(30000):,.2f} meter altitude"
print(txt)

##
# Trying your creativity here
##
def myconverter(x):
    return x * 0.3048

a = input("Masukan angka integer saja: ")
x = float(a)

txt = f"The plane is flying at a {myconverter(x):,.2f} meter altitude"
print(txt)


# Use a comma as a thousand separator
price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

# Formatting Types
# :<	 Left aligns the result (within the available space)
# :>	 Right aligns the result (within the available space)
# :^	 Center aligns the result (within the available space)
# :=	 Places the sign to the left most position
# :+	 Use a plus sign to indicate if the result is positive or negative
# :-	 Use a minus sign for negative values only
# : 	 Use a space to insert an extra space before positive numbers (and a minus sign before negative numbers)
# :,	 Use a comma as a thousand separator
# :_	 Use a underscore as a thousand separator
# :b	 Binary format
# :c	 Converts the value into the corresponding Unicode character
# :d	 Decimal format
# :e	 Scientific format, with a lower case e
# :E	 Scientific format, with an upper case E
# :f	 Fix point number format
# :F	 Fix point number format, in uppercase format (show inf and nan as INF and NAN)
# :g	 General format
# :G	 General format (using a upper case E for scientific notations)
# :o	 Octal format
# :x	 Hex format, lower case
# :X	 Hex format, upper case
# :n	 Number format
# :%	 Percentage format


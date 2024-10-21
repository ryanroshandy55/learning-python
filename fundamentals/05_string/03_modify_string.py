# Modify strings

# transform text to upper
# the text transform to HELLO, WORLD
a = "hello, world"
print(a.upper())

# transform text to lower
a = "Hello, World!"
print(a.lower())

# Remove whitespace with strip
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

# replace string (to replace string with another string, 
# if the string same, all the string will replace)
a = "Hello, World!"
print(a.replace("H", "J"))

# split string
a = "Hello, World!"
print(a.split(","))     # return ['Hello', 'World!']

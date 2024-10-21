# string can used single or double quotation
print('hello world')
print("hello world")

# if want to use quotes inside string
print("He called 'The Doctor'")
print('He called "The Doctor"')

# Assign String to a Variable
a = "Hello"
print(a)

# Multiline string
# triple of single quotes
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# triple of double quotes
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are Arrays
a = "Hello, World!"
print(a[1])

# Looping through a string
for x in "banana":
    print(x)

# Check string length
a = "Hello, World!"
print(len(a))

# Check string
txt = "The best things in life are free!"
print("free" in txt)

# if statement
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
    
# Check if not
txt = "The best things in life are free!"
print("expensive" not in txt)

# print only if "expensive" is NOT present
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
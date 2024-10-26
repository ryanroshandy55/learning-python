# Python conditions and if statements
# pyython supports the usual logical form math:
    # Equals: a == b
    # Not Equals: a != b
    # Less than: a < b
    # Less than or equal to: a <= b
    # Greater than: a > b
    # Greater than or equal to: a >= b
# These conditions can be used in several ways, most commonly in "if statements" and loops
# An "if statement" is written by using the if keyword

a = 33
b = 200
if b > a:
    print("b is greater than a")
    
#  Indentation
#  remember after if statements:
#  the structure of code in python use 1 tabular/indent
#  this is a sensitive case and must consistant on writing if.. else..
# a = 33
# b = 200
# if b > a:
# print("b is greater than a") # you will get an error, because without indent

# Elif
# the elif keyword is Python's way of saying "if the previous conditions were not true, the try this conditions".
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  
# else
# The else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  
# In this example a is greater than b, so the first condition is not true, also the elif condition is not true, 
# so we go to the else condition and print to screen that "a is greater than b".
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
  
# Short hand if .. else
a = 2
b = 330
print("A") if a > b else print("B")

# Having multiple statement in the same line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
# Test if a is greater than b, AND if c is greater than a
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:
# Test if a is greater than b, OR if a is greater than C
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
  
# Not
# the NOT keyword is a logical operator, and is used to reverse ther result of the conditional statment
# Test if a is NOT greater than b
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

# Nested if
# You can have if statements inside if statements, this is called nested if statements.
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# The pass statement
a = 33
b = 200

if b > a:
  pass
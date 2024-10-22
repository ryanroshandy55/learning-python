# Global variable
def value():
    global x
    x = 3

def nine():
    global x
    x = 9

# Python Assignment Operators
# =

# +=
value()
for i in range (x):
    x+=3
    print(i,"=",x)

# -=
value()
print("-=")
for i in range (x):
    x-=3
    print(i,"=",x)
    
# *=
value()
print("*=")
for i in range (x):
    x*=3
    print(i,"=",x)

# /=
value()
print("/=")
for i in range (x):
    x/=3
    print(i,"=",x)

# %=
value()
print("%=")
for i in range (x):
    for j in range (3):
        x%=3
    print(i,"=",x)
    x+=1
# //=
nine()
print("// =", x//3)
# &=
# |=
# ^=

# This is operator for signed shift on binary number
# nine() / x = 9 
# 00000000001001
# >>=
nine()
x >>= 1
print(x)
# Move to right / shift binary counted 1
# 00000000000100

# Invert of >>, binary is shift to left <<
# <<=
nine()
x = 5
x <<= 12
print(x)

# :=
nine()
print(x:=3)
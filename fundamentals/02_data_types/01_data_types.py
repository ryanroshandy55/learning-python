
x = "Hello World"	#string
print(type(x))

x = 20	# int
print(type(x))

x = 20.5	#float	
print(type(x))

x = 1j	#complex	
print(type(x))

x = ["apple", "banana", "cherry"]	#list	
print(type(x))

x = ("apple", "banana", "cherry")	#tuple	
print(type(x))

x = range(6)	#range
print(type(x))

x = {"name" : "John", "age" : 36}	#dict
print(type(x))

x = {"apple", "banana", "cherry"}	#set	
print(type(x))

x = frozenset({"apple", "banana", "cherry"})	#frozenset	
print(type(x))

x = True	#bool
print(type(x))

x = b"Hello"	#bytes
print(type(x))

x = bytearray(5)	#bytearray
print(type(x))

x = memoryview(bytes(5))	#memoryview
print(type(x))

x = None	#NoneType
print(type(x))

# if you want to make specific data
# just use this code
# variables = specific_type()
#####
# We know list is x = ["Apple", "Banana", "Cherry"]
# if specific be this:
# ex: x = list(("Apple", "Banana", "Cherry"))
#####
# We know frozenset is x = ({"Apple", "Banana", "Cherry"})
# if specific be this:
# ex: x = frozenset(("Apple", "Banana", "Cherry"))
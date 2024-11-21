# Python is an object oriented programming language
# Almost everything in Python is an object., with its properties and methods.
# A class i s like an object constructor, or a "blueprient" for creating objects

# create class
class MyClass:
    x = 5

# create object
p1 = MyClass()
print(p1.x)



# The __init__ functions

# The example above are classes and object in their simplest form, and are not really useful in real life applications
# To understand the meaning of classes we have to understand the built in __init__() function.
# All classes have a function called __init__() , which is always executed when the class is being initiated
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = Person("John", 36)

print(p1.name)
print(p1.age)
print(p1)

# output = 
# John
# 36
#<__main__.Person object at 0x000001B0759EE410

# The __str__() Function

# The __str__() function controls what should be returned when the class object is prepresented as a string
# If the __str__() function is not set, the string representation of the object is returned:

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# Output
# John(36)


# Object Methods
class Person:
    def __init__ (self, name, age):
        self.name = name
        self.age = age
    
    def myfunc(self):
        print("Hello my name is " + self.name, "My age is", self.age)

p1 = Person("John", 36)
p1.myfunc()

# Output
# Hello my name is John My age is 36


# The self Parameter

# The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class:
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any function in the class:

class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    def myfunc(abc):
        try:
            print("Hello my name is", abc.name, ". My age is", abc.age)
        except:
            print("there is something wrong with your code value, check again your command")

p1 = Person("John", 36)
p1.myfunc()

# Output
# Hello my name is John . My age is 36


# You can delete it property
# Ex
del p1.age
p1.myfunc()
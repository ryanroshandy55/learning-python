# Python Inheritance

# Inheritance allows us to define a class that inherits all the methods and properties from another class
    # Parent class is the class being inherited from, also called base class.
    # Child class is the class that inherits from another class, also called derived class


# Create a Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
                
    def printname (self):
        print(self.firstname, self.lastname)
        

# Use the Person class to create an object, and then execute the printname method:
x = Person("John", "Doe")
x.printname()

# Output
# John Doe


# Create a Child Class
# To create a class that inherits the functionality from another class, 
# send the parent class as a parameter when creating the child class:

class Student(Person):
    pass

x = Student("Mike", "Olsen")
x.printname()

# Output
# Mike Olsen


# Add the __init__() function
# So far we have created a child class that inherits the properties and methods from its parent.
# We want to add the __init__() function to the child class (instead of the pass keyword)

# Note: The __init__() function is called automatically every time the class is being used to create a new object

# To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function:
class Student(Person):
    def __init__(self, fname, lname):
        # add property etc.
        Person.__init__(self, fname, lname)


# Use super() Function
# Python also has a super() function that will make the child class inherit all the methods and properties from its parent:
class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        # add properties
        self.graduationyear = 2019

x = Student("Mike", "Olsen")
print(x.graduationyear)

# add year parameter
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        # add properties
        self.graduationyear = year

x = Student("Mike", "Olsen", 2020)
print(x.graduationyear)

# Add methods
class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year
    
    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)
    
x = Student("Mike", "Olsen", 2020)
x.welcome()
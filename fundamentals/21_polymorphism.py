# Python Polymorphism
# The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators 
# with the same name that can be executed on many objects or classes.

# Function Polymorphism
# and example of a python function that can be used on different objects is the len() function.

# String
x = "Hello world!"

print(len(x))

# Tuple
mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

# Dictionary
thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year" : 1964
}

print(len(thisdict))


# Class Polymorphism

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Drive!")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
    def move(self):
        print("Sail!")
        
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Fly!")
    
car1 = Car("Ford", "Mustang")   # create a Car Class
boat1 = Boat("Ibiza", "Touring 20")   # create a Boat Class
plane1 = Plane("Boeing", "747")   # create a Plane Class

for x in (car1, boat1, plane1):
    x.move()

print(" ")


# Inheritance Class Polymorphism
# Can we use polymorphism within classes with child classes with the same name?
# Yes, We can use classes with child classes combined with polymorphism there
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")

class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")   # create a Car Class
boat1 = Boat("Ibiza", "Touring 20")   # create a Boat Class
plane1 = Plane("Boeing", "747")   # create a Plane Class

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    print("Combined:", x.brand, x.model)
    x.move()
    print(" ")
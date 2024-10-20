# class parent_class:
# #Body of parent class
#     pass

# class child_class(parent_class):
#     # inherits the parent class
#     # Body of child

class Human:    # Parent class
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def description(self):
        print(f"Hey! My name is {self.name} and my age is {self.age} years old")

class Boy(Human): # Child class
    def schoolName(self, schoolname):
        print(f"I study in {schoolname}")

b = Boy('Edcorner', 32, 'Male')
b.description()
b.schoolName("MIT")

h = Human("Ryan", 22, "male") # Child class
h.description()
h.schoolName("IBIK")
class Human:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def description(self):
        print(f"Hey! my name is {self.name}, i'm a {self.gender} and i'm {self.age} years old")
    
    def code(self):
        print("i can code")

class Girl(Human):
    def codecode(self):
        print("I can teach you about code")
    def activity(self):
        super().code()

g = Girl('Cantona', 21, 'Girl')
g.description()
g.activity()
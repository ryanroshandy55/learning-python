class Human:
    species = "Homo Sapiens"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender


x = Human("Ryan", 32, "Male")
y = Human("Ryan", 30, "Female")

# Learning Python OOPS
# class Human:
#     #class attribute
#     species = "Homo Sapiens"

print(x.name)
print(y.name)

print(f"Hi! My name is {x.name}. I am a {x.gender}, and I am {x.age} years old")
print(f"Hi! My name is {y.name}. I am a {y.gender}, and I am {y.age} years old")

Human.species = "Homo sapiens"
obj = Human("Edcorner", 32, "Male")
print(obj.species)

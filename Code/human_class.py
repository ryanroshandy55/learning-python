# Training to Code


class Human:
    # class attribute
    species = "Homo Sapiens"

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    # Instance Method
    def speak(self):
        return f"Hello, everyone! I am {self.name}"

    # instance Method
    def eat(self, favouriteDish):
        return f"I love to eat {favouriteDish}!!!"


x = Human("Ryan", 21, "Male")
print(x.speak())
print(x.eat("Salad"))
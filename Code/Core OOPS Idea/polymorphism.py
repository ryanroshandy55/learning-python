# print(len("Roshandy"))
# print(len([1, 2, 3, 4, 5, 6, 7]))
# print(len({"1": "aws", "2": "amazon", "3": "kindle"}))

# x = 5 + 5
# y = 'python' + ' programming'
# z = 3.5 + 3
# print(x, y, z)
# print(x)
# print(y)
# print(z)

# polymorphism

class lion:
    def color(self):
        print("The lion is yellow coloured!")

    def eats(self):
        print("The lion eats a lot!")


class deer:
    def color(self):
        print("The deer is orange coloured!")

    def eats(self):
        print("The deer eats less!")


lio = lion()
dee = deer()
for animal in (lio, dee):
    animal.color()
    animal.eats()

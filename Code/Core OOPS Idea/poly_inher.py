class Shape:
    def no_of_sides(self):
        pass

    def three_dimensional(self):
        print("I'm three_dimensional")


class Rectangle(Shape):
    def no_of_sides(self):
        print("I have 4 sides. I am Rectangle class")


class Polygon(Shape):
    def no_of_sides(self):
        print("I have 3 sides. I am from Polygon class")


# Create an object of Square class
re = Rectangle()
# Override the no_of_sides of parent class
re.no_of_sides()

# Create an object of triangle class
po = Polygon()
# Override the no_of_sides of parent class
po.no_of_sides()
from pythonOOP import Circle

c1 = Circle(2.1)
print(c1)
print(c1.get_area())
print(c1.radius)

print(str(c1))
print(repr(c1))

c2 = Circle()
print(c2)

class Circle:
    """A Circle instance models a circle with a radius"""
    pass

class Circle:
    """A Circle instance models a circle a radius"""
    
    def __init__(self, radius=1.0):
        self.radius = radius
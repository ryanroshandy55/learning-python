from math import pi

class Circle:
    """A Circle instance models a circle with a radius"""

    def __init__(self, radius=1.0):
        """Initializer with default radius of 1.0"""
        self.radius = radius # Create an instance variable radius

    def __str__(self):
        """Return a descriptive string for this instance, invoked by print() and str()"""
        return 'This is a circle with radius of {:.2f}'.format(self.radius)
    
    def __repr__(self):
        """Return a formal string that can be used to re-create this instance, invoked by repr()"""
        return 'Circle(radius={})'.format(self.radius)
    
    def get_area(self):
        """Return the area of this Circle instance"""
        return self.radius * self.radius * pi
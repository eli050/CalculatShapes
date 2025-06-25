from Shapes.shape import Shape
from math import *

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def get_area(self):
        return pi * self.radius**2
    def get_perimeter(self):
        return pi * (self.radius * 2)
    def __str__(self):
        return f"Circle with radius {self.radius} and diameter {self.radius * 2}."

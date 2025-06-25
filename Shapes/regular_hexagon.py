from Shapes.square import Square
from math import *


class RegularHexagon(Square):
    def __init__(self, side):
        super().__init__(side)
    def get_area(self):
        return ((3 * sqrt(3))/2) * self._len_sid**2
    def get_perimeter(self):
        return super().get_perimeter() + self._len_sid * 2
    def __str__(self):
        return  "I am regular hexagon "


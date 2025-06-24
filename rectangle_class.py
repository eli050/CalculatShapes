from shapes import Shape

class Rectangle(Shape):
    def __init__(self,len_sid, width_side ):
        self._len_sid = len_sid
        self._width_side = width_side
    def get_area(self):
        return self._len_sid * self._width_side

    def get_perimeter(self):
        return (self._width_side * 2) + (self._len_sid * 2)

    def __str__(self):
        return "I am a rectangle"
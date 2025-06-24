from Shapes.rectangle import Rectangle

class RightAngledTriangle(Rectangle):
    def __init__(self,catheti1:int|float,catheti2:int|float):
        super().__init__(catheti1,catheti2)
    def get_area(self):
        return super().get_area()/2
    def get_perimeter(self):
        return (((self._len_sid**2)+
                (self._width_side**2))**(1/2))+(self._width_side+self._len_sid)
    def __str__(self):
        return "i am right angled triangle"


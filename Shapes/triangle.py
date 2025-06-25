from Shapes.rectangle import Rectangle

class RightAngledTriangle(Rectangle):
    def __init__(self,base:int|float,height:int|float):
        super().__init__(base,height)
    def get_area(self):
        return super().get_area()/2
    def get_perimeter(self):
        return (((self._len_sid**2)+
                (self._width_side**2))**(1/2))+(self._width_side+self._len_sid)
    def __str__(self):
        return f"A right-angled triangle with a base of length {self._len_sid} and a height of length {self._width_side}"


from Shapes.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self,side:int|float):
        super().__init__(side,side)
    def __str__(self):
        return f"Square with side length {self._len_sid}"


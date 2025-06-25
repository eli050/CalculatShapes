from __future__ import annotations
from abc import ABC,abstractmethod


class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def __add__(self, other:Shape):
        return self.get_area() + other.get_area()

    def __sub__(self, other: Shape):
        return self.get_area() - other.get_area()

    def __eq__(self, other:Shape):
        return self.get_area() == other.get_area()

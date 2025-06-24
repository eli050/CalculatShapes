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

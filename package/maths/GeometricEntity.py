from abc import abstractmethod
from package.exceptions.Exceptions import *

class GeometricEntity():
    def __init__(self, name, fillColor):

        self.setName(name)
            
        self._fillColor = fillColor

    def getName(self):
        return self._name
    
    def getFillColor(self):
        return self._fillColor
    
    def setName(self, name):
        if len(name) > 0 or len(name)<=10:
            self._name = name
        else:
            raise InvalidName('The name must be 0 to 10 characters long.')
            
    def setFillColor(self, fillColor):
        self._fillColor = fillColor

    @abstractmethod
    def model(self):
        pass
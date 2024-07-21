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
        if len(name) > 0 and len(name)<=10:
            self._name = name
        else:
            raise InvalidName('The name must be 0 to 10 characters long.')
            
    def setFillColor(self, fillColor):
        self._fillColor = fillColor

    @abstractmethod
    def model(self):
        pass
    
    def info(self):
        return {
			"Type": self.__class__.__name__,
            "Name": self._name,
            "Fill Color": self._fillColor,
            "Points": f'{list(map(lambda x: x.getPoint(), self.getPoints()))}'
		}
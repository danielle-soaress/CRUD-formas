from abc import abstractmethod

class GeometricEntity():
    def __init__(self, name, fillColor):
        self._name = name
        self._fillColor = fillColor

    def getName(self):
        return self._name
    
    def getFillColor(self):
        return self._fillColor
    
    def setName(self, name):
        self._name = name

    def setFillColor(self, fillColor):
        self._fillColor = fillColor

    @abstractmethod
    def model(self):
        pass
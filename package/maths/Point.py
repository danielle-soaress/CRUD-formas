import math

class Point():
    def __init__(self, name, coordX, coordY, fillColor = '#000'):
        self.__name = name
        self.__coordX = coordX
        self.__coordY = coordY
        self.__fillColor = fillColor
    
    def getName(self):
        return self.__name

    def getFillColor(self):
        return self.__fillColor

    def setCoordX(self,newCoord):
        self.__coordX = newCoord

    def getCoordX(self):
        return self.__coordX   

    def getCoordY(self):
        return self.__coordY

    def setCoordY(self, newCoord):
        self.__coordY = newCoord

    def getPoint(self):
        return (self.__coordX,self.__coordY)

    def distanceTo(self, other):
        return math.sqrt((self.__coordX - other.getCoordX()) ** 2 + (self.__coordY - other.getCoordY()) ** 2)

    def info(self):
        return f'{self.__name}: ({self.__coordX}, {self.__coordY})'
    
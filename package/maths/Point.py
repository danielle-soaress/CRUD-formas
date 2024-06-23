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

    # methods that work with relation between this point and others

    def ArePointsDifferent(self, other):
        if self.__coordX == other.getCoordX() and self.__coordY == other.getCoordY():
            return False
        return True
    
    def sort2Points(self, other):
        x1, y1 = self.__coordX, self.__coordY
        x2, y2 = other.getCoordX(), other.getCoordY()
    
        # Comparação das coordenadas x
        if x1 < x2:
            return self, other
        elif x1 > x2:
            return other, self
        else:
            # Se as coordenadas x são iguais, comparar as coordenadas y
            if y1 < y2:
                return self, other
            else:
                return other, self

    def distanceTo(self, other):
        return math.sqrt((self.__coordX - other.getCoordX()) ** 2 + (self.__coordY - other.getCoordY()) ** 2)
    
    def medianBetween(self, other):
        mx = (self.__coordX + other.getCoordX()) / 2
        my = (self.__coordY + other.getCoordY()) / 2
        return (mx, my)
    
    # other methods
    def distanceFromOrigin(self):
        return math.sqrt(self.__coordX ** 2 + self.__coordY ** 2)

    def info(self):
        return f'{self.__name}: ({self.__coordX}, {self.__coordY})'
    
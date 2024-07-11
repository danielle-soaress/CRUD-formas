import math

from package.maths.GeometricEntity import GeometricEntity
from package.exceptions.Exceptions import InvalidAction

class Point(GeometricEntity):
    def __init__(self, name, coordX, coordY, fillColor = '#000'):
        super().__init__(name, fillColor)
        self.__coordX = coordX
        self.__coordY = coordY

        if not self.isAPoint():
            raise InvalidAction("Invalid point. Certify if the numbers are integers.")


    def getCoordX(self):
        return self.__coordX   

    def getCoordY(self):
        return self.__coordY

    def getPoint(self):
        return (self.__coordX,self.__coordY)

    def isAPoint(self):
<<<<<<< HEAD
        if (self.__coordX < 0 or self.__coordY < 0):
            return False
        else:
            if not ((isinstance(self.__coordX, int) or (isinstance(self.__coordX, float) and self.__coordX.is_integer()))):
                return False
            elif not ((isinstance(self.__coordY, int) or 
                    (isinstance(self.__coordY, float) and self.__coordY.is_integer()))):
                return False
=======
        if not ((isinstance(self.__coordX, int) or 
                (isinstance(self.__coordX, float) and self.__coordX.is_integer()))):
            return False
        elif not ((isinstance(self.__coordY, int) or 
                (isinstance(self.__coordY, float) and self.__coordY.is_integer()))):
            return False
>>>>>>> 7c5d97ad7519b133910929f96041d8df5f8a9019
        
        return True

    # methods that work with relation between this point and others

    def arePointsDifferent(self, other):
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

    def model(self):
        return (
        f'''
        ------ Basic Information ------------
        Name: {self._name}
        Coordinates: ({self.__coordX}, {self.__coordY})
        Fill Color: {self._fillColor}

        ------ Functions Information --------
        Distance from Origin: {self.distanceFromOrigin():.2f}
        ''')
    
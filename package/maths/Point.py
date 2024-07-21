import math
import textwrap
from package.maths.GeometricEntity import GeometricEntity
from package.exceptions.Exceptions import InvalidAction

class Point(GeometricEntity):
    def __init__(self, name, coordX, coordY, fillColor = '#000'):
        super().__init__(name, fillColor)
        self.__coordX = coordX
        self.__coordY = coordY

        if not self.isAPoint():
            raise InvalidAction("Invalid point.")

    def getCoordX(self):
        return self.__coordX   

    def getCoordY(self):
        return self.__coordY

    def getPoint(self):
        return (self.__coordX,self.__coordY)

    def isAPoint(self):
        if (self.__coordX < 0 or self.__coordY < 0): # the cartesian plane only allows the visualization of positive points
            return False
        else:
            if not ((isinstance(self.__coordX, int) or (isinstance(self.__coordX, float) and self.__coordX.is_integer()))): # the source of PyQt used on UI can only draw integers points
                return False
            elif not ((isinstance(self.__coordY, int) or 
                    (isinstance(self.__coordY, float) and self.__coordY.is_integer()))):
                return False
        
        return True

    # methods that work with relation between this point and others

    def arePointsDifferent(self, other):
        if self.__coordX == other.getCoordX() and self.__coordY == other.getCoordY():
            return False
        return True
    
    def sort2Points(self, other):
        x1, y1 = self.__coordX, self.__coordY
        x2, y2 = other.getCoordX(), other.getCoordY()
        # compare the x coords
        if x1 < x2:
            return self, other
        elif x1 > x2:
            return other, self
            # if x coords are equal, compare the y coords
        else:
            if y1 < y2:
                return self, other
            else:
                return other, self

    @staticmethod
    def distanceTo(p1, p2):
        return math.sqrt((p1.getCoordX() - p2.getCoordX()) ** 2 + (p1.getCoordY() - p2.getCoordY()) ** 2)
    
    @staticmethod
    def lineSegmentProximity(p3, line):
        p1,p2 = line.getPoints()
        d1_2 = Point.distanceTo(p1, p2)
        d1 = Point.distanceTo(p1, p3)
        d2 = Point.distanceTo(p2, p3)
        d1_2_3 = d1 + d2
        return d1_2_3 <= 1.1 * d1_2

    def medianBetween(self, other):
        mx = (self.__coordX + other.getCoordX()) / 2
        my = (self.__coordY + other.getCoordY()) / 2
        return (mx, my)

    # other methods
    def distanceFromOrigin(self):
        return math.sqrt(self.__coordX ** 2 + self.__coordY ** 2)

    def model(self):
        return textwrap.dedent(
        f'''
        -------- Basic Information ----------
        Name: {self._name}
        Coordinates: ({self.__coordX}, {self.__coordY})
        Fill Color: {self._fillColor}

        ------ Functions Information --------
        Distance from Origin: {self.distanceFromOrigin():.2f}
        ''')
    
    def info(self):
        return {
            "Type": self.__class__.__name__,
            "Name": self._name,
            "Fill Color": self._fillColor,
            "Point": (self.__coordX, self.__coordY)
        }
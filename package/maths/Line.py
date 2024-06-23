import math
from package.exceptions.Exceptions import InvalidShape
from package.maths.Point import Point

class Line():
    def __init__(self, name, p1, p2, fillColor = '#000'):
        self.__name = name
        self.__point1 = p1
        self.__point2 = p2
        self.__fillColor = fillColor # in a line, 'fillColor' is the fill of line points
        
        if not self.isLine():
            raise InvalidShape("A line can't have identical points.")

    # getters and setters
    def getName(self):
        return self.__name

    def getFillColor(self):
        return self.__fillColor

    def setPoint1(self, newP1):
        self.__point1 = newP1
    
    def setPoint2(self, newP2):
        self.__point1 = newP2

    def getPoint1(self):
        return self.__point1
    
    def getPoint2(self):
        return self.__point2
    
    def getPoints(self):
        return self.__point1.sort2Points(self.__point2)
    
    # to verify if the points can form a line
    def isLine(self):
        return True if self.__point1.ArePointsDifferent(self.__point2) else False
    
    # to verify if a point is on Line
    def isPointOnLine(self, point):
        return (min(self.__point1.getCoordX(), self.__point2.getCoordX()) <= point.getCoordX() <= max(self.__point1.getCoordX(), self.__point2.getCoordX()) 
                and min(self.__point1.getCoordY(), self.__point2.getCoordY()) <= point.getCoordY() <= max(self.__point1.getCoordY(), self.__point2.getCoordY()))

    # to calculate length, angular coefficient and define de line equation
    def length(self):
        return math.sqrt((self.__point1.getCoordX() - self.__point2.getCoordX())** 2 + (self.__point1.getCoordY() - self.__point2.getCoordY()) ** 2)
    
    def angularCoefficient(self):
        # i will compare the angular coefficient of each line to define if they are parallels.

        if (self.__point2.x() - self.__point1.x()) == 0: 
            return None     # vertical line
                            # if the line is horizontal, the angular coefficient will be 0. 

        m = (self.__point2.getCoordY() -  self.__point1.getCoordY())/(self.__point2.getCoordX() -  self.__point1.getCoordX())
        return m

    def equation(self):

        p1, p2 = self.__point1.sort2Points(self.__point2)

        if p1.getCoordX() == p2.getCoordX(): # vertical line
            return f'f(x) = {p1.getCoordX()}'
        elif p1.getCoordY() == p2.getCoordY(): # horizontal line
            return f'f(x) = {p1.getCoordY()}'
        else:
            m = self.angularCoefficient()
            b = p1.getCoordY() - m * p1.getCoordX()
            return f"y = {m:.2f}x + {b:.2f}"
        
    # relations with another lines
    def areParallels(self, other):
        return self.angularCoefficient() == other.angularCoefficient()

    def intersection(self, other):
        p1, p2 = self.__point1.sort2Points(self.__point2)
        p3, p4 = other.getPoint1().sort2Points(other.getPoint2())

        # angular coefficients
        m1 = self.angularCoefficient()
        m2 = other.angularCoefficient()

        # parallels lines
        if m1 == m2:
            return None

        # Cálculo do ponto de interseção
        if m1 is None:  # self is vertical
            x = p1.x()
            y = m2 * (x - p3.x()) + p3.y()
        elif m2 is None:  # other is vertical
            x = p3.x()
            y = m1 * (x - p1.x()) + p1.y()
        else:
            x = (m1 * p1.x() - p1.y() - m2 * p3.x() + p3.y()) / (m1 - m2)
            y = m1 * (x - p1.x()) + p1.y()

        intersection_point = Point(int(x), int(y))

        if self.isPointOnSegment(intersection_point) and other.isPointOnSegment(intersection_point):
            return intersection_point
        return None

    def info(self): ######################### editar informação depois
        return f'{self.__name}: '
    
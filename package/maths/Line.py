import math
import textwrap
from package.maths.Point import Point
from package.maths.GeometricEntity import GeometricEntity
from package.exceptions.Exceptions import InvalidAction

# in this file, there are two classes: Line and SegmentLine
# a line is infinite, while a line segment is finite and has a length.

class Line(GeometricEntity):
    def __init__(self, name, p1, p2, fillColor = '#000'):
        super().__init__(name, fillColor) # in a line, 'fillColor' is the fill of line points
        self._points = [p1, p2]
        
        if not self.isLine():
            raise InvalidAction("Invalid Line. Certify if the numbers are integers.")

    # getters and setters

    def setPoint1(self, newP1):
        self._points[0] = newP1
    
    def setPoint2(self, newP2):
        self._points[1] = newP2

    def getPoint1(self):
        return self._points[0]
    
    def getPoint2(self):
        return self._points[1]
    
    def getPoints(self):
        return self._points[0].sort2Points(self._points[1])
    
    # to verify if the points can form a line
    def isLine(self):
        return True if self._points[0].arePointsDifferent(self._points[1]) else False
    
    # to verify if a point is on Line
    def isPointOnLine(self, point):
        return (min(self._points[0].getCoordX(), self._points[1].getCoordX()) <= point.getCoordX() <= max(self._points[0].getCoordX(), self._points[1].getCoordX()) 
                and min(self._points[0].getCoordY(), self._points[1].getCoordY()) <= point.getCoordY() <= max(self._points[0].getCoordY(), self._points[1].getCoordY()))

    # to calculate angular coefficient and define de line equation
    def angularCoefficient(self):
        # i will compare the angular coefficient of each line to define if they are parallels.

        if (self._points[1].getCoordX() - self._points[0].getCoordX()) == 0: 
            return None     # vertical line
                            # if the line is horizontal, the angular coefficient will be 0. 

        m = (self._points[1].getCoordY() -  self._points[0].getCoordY())/(self._points[1].getCoordX() -  self._points[0].getCoordX())
        return m

    def equation(self):

        p1, p2 = self._points[0].sort2Points(self._points[1])

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
        p1, p2 = self._points[0].sort2Points(self._points[1])
        p3, p4 = other.getPoint1().sort2Points(other.getPoint2())

        # angular coefficients
        m1 = self.angularCoefficient()
        m2 = other.angularCoefficient()

        # parallels lines
        if m1 == m2:
            return "The lines don't intersect"

        # Cálculo do ponto de interseção
        if m1 is None:  # self is vertical
            x = p1.getCoordX()
            y = m2 * (x - p3.getCoordX()) + p3.getCoordY()
        elif m2 is None:  # other is vertical
            x = p3.getCoordX()
            y = m1 * (x - p1.getCoordX()) + p1.getCoordY()
        else:
            x = (m1 * p1.getCoordX() - p1.getCoordY() - m2 * p3.getCoordX() + p3.getCoordY()) / (m1 - m2)
            y = m1 * (x - p1.getCoordX()) + p1.getCoordY()

        intersection_point = Point('intersection', int(x), int(y))

        if self.isPointOnLine(intersection_point) and other.isPointOnLine(intersection_point):
            return intersection_point.getPoint()
        return "The lines don't intersect"

    def model(self):
        return textwrap.dedent(
        f'''
        ------ Basic Information ------------
        Name: {self._name}
        Fill Color: {self._fillColor}
        Points: {f'{self._points[0].getPoint()}, {self._points[1].getPoint()}'}

        ------ Functions Information --------
        Angular Coefficient: {self.angularCoefficient():.2f}
        Equation: {self.equation()}
        '''
        )

class LineSegment(Line):
    def __init__(self, name, p1, p2, fillColor = '#000'):
        super().__init__(name, p1, p2, fillColor)
        
        if not self.isLine():
            raise InvalidAction("Invalid Line Segment. Certify if the numbers are integers.")
        
    def length(self):
        result = math.sqrt((self._points[0].getCoordX() - self._points[1].getCoordX())** 2 + (self._points[0].getCoordY() - self._points[1].getCoordY()) ** 2)
        return result
    
    def model(self):
        return textwrap.dedent(
        f'''
        ------ Basic Information ------------
        Name: {self._name}
        Fill Color: {self._fillColor}
        Points: {f'{self._points[0].getPoint()}, {self._points[1].getPoint()}'}

        ------ Functions Information --------
        Length: {self.length():.2f}
        Angular Coefficient: {self.angularCoefficient():.2f}
        Equation: {self.equation()}
        '''
        )
from package.maths.Shape import Shape
from package.exceptions.Exceptions import InvalidShape
from itertools import combinations
import math

class Rectangle(Shape):
    def __init__(self, id, point1, point2, point3, point4, fillColor):
        super().__init__(id,[point1,point2,point3,point4], fillColor)
        if not self.isARect():
            raise InvalidShape("The points did not form a rectangle.")
            
    def getWidth(self):
        return abs(self._points[3].getCoordX() - self._points[0].getCoordX())
    
    def getHeight(self):
        return abs(self._points[3].getCoordY() - self._points[0].getCoordY())

    def isARect(self):
        # calculate all distances of points from each other
        distances = [p1.distanceTo(p2) for p1, p2 in combinations(self._points, 2)]
        distances.sort()

        # a rectangle should have 4 equal shorter sides (2 pairs of sides) and 2 equal longer sides (diagonals)
        if not (distances[0] == distances[1] and 
            distances[2] == distances[3] and 
            distances[4] == distances[5]):
            return False
        return True
    
class Triangule(Shape):
    def __init__(self, id, point1, point2, point3, fillColor):
        super().__init__(id,[point1,point2,point3], fillColor)
        if not self.isATriangule():
            raise InvalidShape("The points did not form a triangule.")
    
    def isATriangule(self):
        # the points can't be collinear. For check this, we can use the same formula
        # used to calculate the area.

        triangule_area = self.area()
        
        return True if triangule_area>0 else False
    
    def area(self):
        p1, p2, p3 = self._points[0],self._points[1],self._points[2]

        triangule_area = 0.5 *abs(p1.getCoordX()*(p2.getCoordY() - p3.getCoordY()) + #determinant formula for area
                        p2.getCoordX()*(p3.getCoordY() - p1.getCoordY()) +
                        p3.getCoordX()*(p1.getCoordY() - p2.getCoordY()))
        
        return triangule_area

    def perimeter(self):
        side1 = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
        side2 = math.sqrt((self.x3 - self.x2) ** 2 + (self.y3 - self.y2) ** 2)
        side3 = math.sqrt((self.x1 - self.x3) ** 2 + (self.y1 - self.y3) ** 2)
        return side1 + side2 + side3

class Circle(Shape):
    def __init__(self, id, point1, radius, fillColor):
        super().__init__(id,[point1], fillColor)
        self.__radius = radius
        if not self.isACircle():
            raise InvalidShape("Please, insert a non-null radius value. ")
    
    def getRadius(self):
        return self.__radius

    def getDiameter(self):
        return self.__radius*2

    def isACircle(self):
        if self.__radius <= 0:
            return False
        return True 

    def area(self):
        return math.pi*(self.__radius**2)

    def perimeter(self):
        return 2*math.pi*self.__radius


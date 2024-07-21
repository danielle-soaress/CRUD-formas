import math
import textwrap

from package.maths.Shape import Shape
from package.maths.Point import Point
from itertools import combinations
from package.exceptions.Exceptions import *

class Rectangle(Shape):
    def __init__(self, name, point1, point2, point3, point4, fillColor):
        super().__init__(name,[point1,point2,point3,point4], fillColor)
        if not self.isARect():
            raise InvalidAction("The points did not form a rectangle.")
            
    def width(self):
        return abs(self._points[3].getCoordX() - self._points[0].getCoordX())
    
    def height(self):
        return abs(self._points[3].getCoordY() - self._points[0].getCoordY())

    def isARect(self):
        # calculate all distances of points from each other
        distances = [Point.distanceTo(p1,p2) for p1, p2 in combinations(self._points, 2)]
        distances.sort()

        # a rectangle should have 4 equal shorter sides (2 pairs of sides) and 2 equal longer sides (diagonals)
        if not (distances[0] == distances[1] and 
            distances[2] == distances[3] and 
            distances[4] == distances[5]):
            return False
        return True
    
    def area(self):
        return self.width() * self.height()

    def perimeter(self):
        return self.width()*2+self.height()*2
    
    def model(self):
        return textwrap.dedent(
        f'''
        -------- Basic Information ----------
        Name: {self._name}
        Fill Color: {self._fillColor}
        Points: {list(map(lambda x: x.getPoint(), self.getPoints()))}

        ------ Functions Information --------
        Width: {self.width()}
        Height: {self.height()}
        Area: {self.area():.2f}
        Perimeter: {self.perimeter():.2f}
        '''
        ) 

class Triangle(Shape):
    def __init__(self, name, point1, point2, point3, fillColor):
        super().__init__(name, [point1, point2, point3], fillColor)
        if not self.isATriangle():
            raise InvalidAction("The points did not form a Triangle.")
    
    def isATriangle(self): 
        # the points can't be collinear. For check this, we can use the same formula
        # used to calculate the area.
        Triangle_area = self.area()
        return Triangle_area > 0
    
    def sides(self):
        p1, p2, p3 = self._points[0], self._points[1], self._points[2]
        side1 = math.sqrt((p2.getCoordX() - p1.getCoordX()) ** 2 + (p2.getCoordY() - p1.getCoordY()) ** 2)
        side2 = math.sqrt((p3.getCoordX() - p2.getCoordX()) ** 2 + (p3.getCoordY() - p2.getCoordY()) ** 2)
        side3 = math.sqrt((p1.getCoordX() - p3.getCoordX()) ** 2 + (p1.getCoordY() - p3.getCoordY()) ** 2)
        return side1, side2, side3
    
    def area(self):
        p1, p2, p3 = self._points[0], self._points[1], self._points[2]
        Triangle_area = 0.5 * abs(p1.getCoordX()*(p2.getCoordY() - p3.getCoordY()) + #determinant formula for area
                                   p2.getCoordX()*(p3.getCoordY() - p1.getCoordY()) +
                                   p3.getCoordX()*(p1.getCoordY() - p2.getCoordY()))
        return Triangle_area
    
    def perimeter(self):
        side1, side2, side3 = self.sides()
        return side1 + side2 + side3

    def hypotenuse(self):
        sides = self.sides()
        return max(sides)

    def classify(self):
        sides = self.sides()
        unique_sides = len(set(sides))

        if unique_sides == 1:
            return "Equilateral"
        elif unique_sides == 2:
            return "Isosceles"
        else:
            return "Scalene"
    
    def angles(self):
        side1, side2, side3 = self.sides()
        angle1 = math.acos((side2**2 + side3**2 - side1**2) / (2 * side2 * side3))
        angle2 = math.acos((side1**2 + side3**2 - side2**2) / (2 * side1 * side3))
        angle3 = math.acos((side1**2 + side2**2 - side3**2) / (2 * side1 * side2))
        return math.degrees(angle1), math.degrees(angle2), math.degrees(angle3)

    def model(self):
        return textwrap.dedent(
            f'''
            -------- Basic Information ----------
            Name: {self._name}
            Fill Color: {self._fillColor}
            Points: {list(map(lambda x: x.getPoint(), self.getPoints()))}

            ------ Functions Information --------
            Classification: {self.classify()}
            Area: {self.area():.2f}
            Perimeter: {self.perimeter():.2f}
            Hypotenuse: {self.hypotenuse():.2f}
            Sides: {', '.join([f"{side:.2f}" for side in self.sides()])}
            Internal Angles: {', '.join([f"{angle:.2f}" for angle in self.angles()])}
            '''
        )

class Circle(Shape):
    def __init__(self, name, point1, radius, fillColor):
        super().__init__(name,[point1], fillColor)
        self.__radius = radius

        if not self.isACircle():
            raise InvalidAction("The radius value must be between 0 to 10.")
    
    def getRadius(self):
        return self.__radius

    def diameter(self):
        return self.__radius*2

    def isACircle(self):
        if not ((isinstance(self.__radius, int) or 
                (isinstance(self.__radius, float) and self.__radius.is_integer()))):
            return False
        if self.__radius <= 0 or self.__radius > 10:
            return False

        return True 

    def area(self):
        return math.pi*(self.__radius**2)

    def perimeter(self):
        return 2*math.pi*self.__radius

    def model(self):
        return textwrap.dedent(
        f'''
        -------- Basic Information ----------
        Name: {self._name}
        Fill Color: {self._fillColor}
        Points: {list(map(lambda x: x.getPoint(), self.getPoints()))}

        ------ Functions Information --------
        Radius: {self.__radius}
        Diameter: {self.diameter()}
        Area: {self.area():.2f}
        Perimeter: {self.perimeter():.2f}
        '''
        )
    
    def info(self):
        return {
            "Type": self.__class__.__name__,
            "Name": self._name,
            "Fill Color": self._fillColor,
            "Points": f'{list(map(lambda x: x.getPoint(), self.getPoints()))}',
            "Radius": self.__radius
        }
    
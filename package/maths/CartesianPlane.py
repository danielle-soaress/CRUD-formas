from package.maths.Shape import Shape
from package.maths.Shapes import *
from package.maths.Point import Point
from package.maths.Line import Line
from package.exceptions.Exceptions import InvalidShape

class CartesianPlane():

    def __init__(self, width = 900, heigth = 600, name = None):
        self.__width = width
        self.__heigth = heigth
        self.__name = name
        self.__figures = []

    def getFigures(self):
        return self.__figures
    
    def getAFigureByName(self, name):
        for figure in self.__figures:
            if figure.getName() == name:
                return figure
        raise InvalidShape('Some point is not on the Cartesian Plane.')
        
    def setFigures(self, newValue):
        self.__figures = newValue

    def addFigure(self, shape: Shape):
        self.__figures.append(shape)

    def deleteFigure(self, shape_name):
        for figure in self.__figures:
            if figure.getName() == shape_name:
                self.__figures.remove(figure)

    def canAddFigure(self, figure):
        for shape in self.__figures:
            if isinstance(shape, Shape) and isinstance(figure, Shape):
                shape_points = list(map(lambda p: ({p.getCoordX()},{p.getCoordY()}), shape.getPoints()))
                figure_points = list(map(lambda p: ({p.getCoordX()},{p.getCoordY()}), figure.getPoints()))

                if isinstance(figure, Rectangle) and isinstance(shape, Rectangle) and figure_points == shape_points:
                    raise InvalidShape("The Rectangle you're trying to create already exists.")
                if isinstance(figure, Triangule) and isinstance(shape, Triangule)and figure_points == shape_points:
                    raise InvalidShape("The Triangule you're trying to create already exists.")
                if isinstance(figure, Circle) and isinstance(shape, Circle) and figure_points == shape_points:
                    raise InvalidShape("The Circle you're trying to create already exists.")
            if isinstance(shape, Point) and isinstance(figure, Point) and shape.getPoint() == figure.getPoint():
                    raise InvalidShape("The Point you're trying to create already existis.")
            if isinstance(shape, Line) and isinstance(figure, Line):
                    p1, p2 = list(map(lambda p: p.getPoint(), figure.getPoints()))
                    p3, p4 = list(map(lambda p: p.getPoint(), shape.getPoints()))
                    if p1 == p3 and p2 == p4:
                        raise InvalidShape("The Line you're trying to create already existis.")

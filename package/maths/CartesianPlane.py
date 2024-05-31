from package.maths.Shape import Shape
from package.maths.Shapes import *
from package.maths.Point import Point
from package.exceptions.Exceptions import InvalidShape

class CartesianPlane():

    def __init__(self, width = 900, heigth = 600, name = None):
        self.__width = width
        self.__heigth = heigth
        self.__name = name
        self.__shapes = []
    
    def addShape(self, shape: Shape):
        self.__shapes.append(shape)

    def getShapes(self):
        return self.__shapes

    def canAddFigure(self, figure):
        print(self.__shapes)

        for shape in self.__shapes:
            if isinstance(shape, Shape) and isinstance(figure, Shape):
                shape_points = list(map(lambda p: ({p.getCoordX()},{p.getCoordY()}), shape.getPoints()))
                figure_points = list(map(lambda p: ({p.getCoordX()},{p.getCoordY()}), figure.getPoints()))

                if isinstance(figure, Rectangle) and isinstance(shape, Rectangle) and figure_points == shape_points:
                    raise InvalidShape("The Rectangle you're trying to create already exists.")
                
                if isinstance(figure, Triangule) and isinstance(shape, Triangule)and figure_points == shape_points:
                    raise InvalidShape("The Triangule you're trying to create already exists.")
                # i need to create another condition: you can't insert a shape inside another. (I don't know if i like this idea)
            if isinstance(shape, Point) and isinstance(figure, Point) and shape.getPoint() == figure.getPoint():
                    raise InvalidShape("The Point you're trying to create already existis.")

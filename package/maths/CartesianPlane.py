from package.maths.Shape import Shape
from typing import List

class CartesianPlane():

    def __init__(self, width = 900, heigth = 600, name = None):
        self.__width = width
        self.__heigth = heigth
        self.__name = name
        self.__shapes: List[shape] = []
    
    def addShape(self, shape: Shape):
        self.__shapes.append(shape)

    def getShapes(self):
        return self.__shapes


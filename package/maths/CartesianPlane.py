from package.maths.Shape import Shape
from package.maths.Shapes import *
from package.maths.Point import Point
from package.maths.Line import *
from package.maths.GeometricEntity import GeometricEntity
from package.exceptions.Exceptions import InvalidAction


class CartesianPlane():
    def __init__(self):
        self.__entities = []

    def setEntities(self, list):
        for i in list:
            if not (isinstance(i, GeometricEntity)):
                print("All objects must be Geometric entities!")
                return 
        
        self.__entities = list
                
    def getEntities(self):  # this function returns all geometric entities
        return self.__entities
    
    def getAEntitieByName(self, name): # this function returns a specific figure
        for entity in self.__entities:
            if entity.getName() == name:
                print(entity)
                return entity
        return None
    
    def getAllClassEntities(self, entityClass):# this function returns all entities that belong to the same class
        if entityClass == 'line':
            result = []
            for entity in self.__entities:
                if isinstance(entity, Line):
                    result.append(entity)
        return result
    
    def reset(self): # this function its important to clean the cartesian plane (remove all entities)
        self.__entities = []

    def addEntity(self, entity):
        try:
            if self.canAddEntity(entity):
                self.__entities.append(entity)
        except InvalidAction as e:
            print('This figure already exists in the Cartesian Plane.')

    def deleteEntity(self, shape_name):
        for entity in self.__entities:
            if entity.getName() == shape_name:
                self.__entities.remove(entity)

    def canAddEntity(self, figure): # this function is important to check if user is adding a different figure 
        for shape in self.__entities:
            if isinstance(shape, Shape) and isinstance(figure, Shape):
                shape_points = list(map(lambda p: ({p.getCoordX()},{p.getCoordY()}), shape.getPoints()))
                figure_points = list(map(lambda p: ({p.getCoordX()},{p.getCoordY()}), figure.getPoints()))

                if isinstance(figure, Rectangle) and isinstance(shape, Rectangle) and figure_points == shape_points:
                    raise InvalidAction("The Rectangle you're trying to create already exists.")
                if isinstance(figure, Triangule) and isinstance(shape, Triangule)and figure_points == shape_points:
                    raise InvalidAction("The Rectangle you're trying to create already exists.")
                if isinstance(figure, Circle) and isinstance(shape, Circle) and figure_points == shape_points:
                    raise InvalidAction("The Rectangle you're trying to create already exists.")
            if isinstance(shape, Point) and isinstance(figure, Point) and shape.getPoint() == figure.getPoint():
                    raise InvalidAction("The Rectangle you're trying to create already exists.")
            if isinstance(shape, Line) and isinstance(figure, Line):
                    p1, p2 = list(map(lambda p: p.getPoint(), figure.getPoints()))
                    p3, p4 = list(map(lambda p: p.getPoint(), shape.getPoints()))
                    if p1 == p3 and p2 == p4:
                        raise InvalidAction("The Rectangle you're trying to create already exists.")
        return True

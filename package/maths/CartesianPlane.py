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
                raise InvalidAction("All objects must be Geometric entities!")
        
        self.__entities = list
                
    def getEntities(self):  # this function returns all geometric entities
        return self.__entities
    
    def getAEntitieByName(self, name): # this function returns a specific figure
        for entity in self.__entities:
            if entity.getName() == name:
                return entity
        return None
    
    def getAllClassEntities(self, entityClass): # this function returns all entities that belong to the same class
        if not isinstance(entityClass, type):
            raise InvalidAction("You must enter a valid class.")
        
        result = []
        for entity in self.__entities:
            if isinstance(entity, entityClass):
                result.append(entity)
        return result
    
    def reset(self): # this function its important to clean the cartesian plane (remove all entities)
        self.__entities = []

    def addEntity(self, entity):
        if self.canAddEntity(entity):
            self.__entities.append(entity)

    def deleteEntity(self, shape_name):
        for entity in self.__entities:
            if entity.getName() == shape_name:
                self.__entities.remove(entity)

    def canAddEntity(self, figure): # this function is important to check if user is adding a different figure 
        for entity in self.__entities:
            if figure.getName() == entity.getName():
                raise InvalidAction("Already exists a geometric entity with this name.")
            else:
                if isinstance(entity, Shape) and isinstance(figure, Shape):
                    entity_points = list(map(lambda p: ({p.getCoordX()},{p.getCoordY()}), entity.getPoints()))
                    figure_points = list(map(lambda p: ({p.getCoordX()},{p.getCoordY()}), figure.getPoints()))

                    if isinstance(figure, Rectangle) and isinstance(entity, Rectangle) and figure_points == entity_points:
                        raise InvalidAction("The Rectangle you're trying to create already exists.")
                    if isinstance(figure, Triangule) and isinstance(entity, Triangule)and figure_points == entity_points:
                        raise InvalidAction("The Rectangle you're trying to create already exists.")
                    if isinstance(figure, Circle) and isinstance(entity, Circle) and figure_points == entity_points:
                        raise InvalidAction("The Rectangle you're trying to create already exists.")
                if isinstance(entity, Point) and isinstance(figure, Point) and entity.getPoint() == figure.getPoint():
                        raise InvalidAction("The Rectangle you're trying to create already exists.")
                if isinstance(entity, Line) and isinstance(figure, Line):
                        p1, p2 = list(map(lambda p: p.getPoint(), figure.getPoints()))
                        p3, p4 = list(map(lambda p: p.getPoint(), entity.getPoints()))
                        if p1 == p3 and p2 == p4:
                            raise InvalidAction("The Rectangle you're trying to create already exists.")
        return True

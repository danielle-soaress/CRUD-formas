class Point():
    def __init__(self, name, coordX, coordY, fillColor = '#000'):
        self.__name = name
        self.__coordX = coordX
        self.__coordY = coordY
        self.__fillColor = fillColor
    
    def getFillColor(self):
        return self.__fillColor

    def setCoordX(self,newCoord):
        self.__coordX = newCoord

    def getCoordX(self):
        return self.__coordX   

    def getCoordY(self):
        return self.__coordY

    def setCoordY(self, newCoord):
        self.__coordY = newCoord

    def getPoint(self):
        return (self.__coordX,self.__coordY)
    def __eq__(self, other):
        return self.__coordX == other.__coordX and self.__coordY == other.__coordY

    def __lt__(self, other):
        return self.__coordX < other.getCoordX()

    def __gt__(self, other):
        return self.__coordY > other.getCoordY()
    
    def __str__(self):
        return f"({self.__coordX}, {self.__coordY})"
class Point():
    def __init__(self, coordX, coordY):
        self.__coordX = coordX
        self.__coordY = coordY
    
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
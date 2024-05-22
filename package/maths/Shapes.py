from package.maths.Shape import Shape

class Rectangle(Shape):
	
    def __init__(self, id, point1, point2, point3, point4, fillColor):
        super().__init__(id,[point1,point2,point3,point4], fillColor)
    
    def getWidth(self):

        return abs(self.rightMostPoint(self._points).getCoordX()-self.leftMostPoint(self._points).getCoordX())
    
    def getHeight(self):
        return abs(self.lowestPoint(self._points).getCoordY()-self.highestPoint(self._points).getCoordY())
    
    def getFillColor(self):
        return self._fillColor

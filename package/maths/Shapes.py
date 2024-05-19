from package.maths.Shape import Shape

class Rectangle(Shape):
	
    def __init__(self, id, points, fillEnabled, fillColor = None):
        if (len(points) == 4):
            super().__init__(id, points, fillEnabled, fillColor)
        else:
            return print("Error: invalid points quantity")

    def width(self):
        return self.rightMostPoint(self._Shape__points).getCoordX() - self.leftMostPoint(self._Shape__points).getCoordX()
    
    def height(self):
        return self.highestPoint(self._Shape__points).getCoordY() - self.lowestPoint(self._Shape__points).getCoordY()
    
    def model(self):
        return (
            f'Id: {self._Shape__id}\n' +
            f'Fill Color: None' if self._Shape__fillEnabled == False else f'Fill Color: {self.__fillColor}'
        )

    def draw(self, cartesianPlane):
        cartesianPlane.drawRect((0,0,0,0), self.leftMostPoint(self._Shape__points).getCoordX(), self.lowestPoint(self._Shape__points).getCoordY(), self.width(), self.height())
	
    def __init__(self, id, points, fillEnabled, fillColor = None):
        if (len(points) == 4):
            super().__init__(id, points, fillEnabled, fillColor)
        else:
            return print("Error: invalid points quantity")

    def width(self):
        return self.rightMostPoint(self._Figure__points).getCoordX() - self.leftMostPoint(self._Figure__points).getCoordX()
    
    def height(self):
        return self.highestPoint(self._Figure__points).getCoordY() - self.lowestPoint(self._Figure__points).getCoordY()
    
    def model(self):
        return (
            f'Id: {self._Figure__id}\n' +
            f'Fill Color: None' if self._Figure__fillEnabled == False else f'Fill Color: {self.__fillColor}'
        )

    def drawRect(self, plane, color, x, y, width, height):
        pygame.draw.rect(plane, color, pygame.Rect(x, y, width, height))
    
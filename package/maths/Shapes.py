from package.maths.Shape import Shape

class Rectangle(Shape):
	
    def __init__(self, id, x,y,width,height, fillColor):
        self.__id = id
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__fillColor = fillColor
        

    def getX(self):
        return self.__x 

    def getY(self):
        return self.__y
    
    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height
    
    def getFillColor(self):
        return self.__fillColor

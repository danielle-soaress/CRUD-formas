from package.UI.UserInterface import UserInterface 

class CartesianPlane():

    def __init__(self, width = 900, height = 600, name = None):
        self.width = width
        self.height = height
        self.name = name
        self.shapes = []

        self.UI = UserInterface(self.width, self.height)
    



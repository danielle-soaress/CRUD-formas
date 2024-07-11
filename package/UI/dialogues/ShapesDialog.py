from package.UI.dialogues.Dialog import Dialog 
from package.maths.Point import Point
from package.maths.Shapes import Rectangle
from package.exceptions.Exceptions import InvalidAction
from package.UI.components.MessageBox import MessageBox

class RectangleDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Rectangle information")


    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            points = self.getData()[1:5]
            print(self.getData())

            rect = Rectangle('rect', 
                    Point('Point 1', points[0][0], points[0][1]), 
                    Point('Point 2', points[1][0], points[1][1]), 
                    Point('Point 3', points[2][0], points[2][1]), 
                    Point('Point 4', points[3][0], points[3][1]), 
                    '#000')
            
            self._ui.getCartesianPlane().canAddEntity(rect) # to verify if this shape already exists in the plane
        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
    

class TrianguleDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Triangule information")


    def AreInputsValid(self):
        super().AreInputsValid()
        points = self.getData()[1:5]
        print(self.getData())

        try:
            rect = Rectangle('rect', 
                    Point('Point 1', points[0][0], points[0][1]), 
                    Point('Point 2', points[1][0], points[1][1]), 
                    Point('Point 3', points[2][0], points[2][1]), 
                    Point('Point 4', points[3][0], points[3][1]), 
                    '#000')
            
            self._ui.getCartesianPlane().canAddEntity(rect) # to verify if this shape already exists in the plane
        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
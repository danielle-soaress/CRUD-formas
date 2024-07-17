from package.UI.dialogues.Dialog import Dialog 
from package.maths.Point import Point
from package.maths.Line import *
from package.maths.Shapes import *
from package.exceptions.Exceptions import *
from package.UI.components.MessageBox import MessageBox
from package.UI.components.Inputs import *
from PyQt5.QtWidgets import QFormLayout


class RectangleDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Rectangle information")
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)


    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            points = self.getData()[1:5]
            

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
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
    
    def defineMainLayout(self):
        self.createEntityForm(4)
    

class TrianguleDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Triangule information")
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)

    def defineMainLayout(self):
        self.createEntityForm(3)

    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            points = self.getData()[1:4]

            triangule = Triangule('triangule', 
                    Point('Point 1', points[0][0], points[0][1]), 
                    Point('Point 2', points[1][0], points[1][1]), 
                    Point('Point 3', points[2][0], points[2][1]), 
                    '#000')
            
            self._ui.getCartesianPlane().canAddEntity(triangule) # to verify if this shape already exists in the plane
        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

class CircleDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Circle information")
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)

    def defineMainLayout(self):
        self.createEntityForm(0,True)

    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            points = self.getData()[1:3]

            circle = Circle('circle', 
                    Point('Point 1', points[0][0], points[0][1]), 
                    points[1],
                    '#000')
            
            self._ui.getCartesianPlane().canAddEntity(circle) # to verify if this shape already exists in the plane
        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
    
class PointDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Point information")
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)

    def defineMainLayout(self):
        self.createEntityForm(1)

    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            data = self.getData()

            p = Point('p1', data[1][0], data[1][1], '#000')
            
            self._ui.getCartesianPlane().canAddEntity(p) # to verify if this shape already exists in the plane
        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

class LineSegmentDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Line information")
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)
        

    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            data = self.getData()

            p = LineSegment(data[0], Point('p1', data[1][0], data[1][1], '#000'), Point('p2', data[2][0], data[2][1]), '#000')
            
            self._ui.getCartesianPlane().canAddEntity(p) # to verify if this shape already exists in the plane
        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

    def defineMainLayout(self):
        self.createEntityForm(2)

class LineDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Line information")
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)
        

    def AreInputsValid(self):
    
        try:
            super().AreInputsValid()
            
            data = self.getData()

            p = Line(data[0], Point('p1', data[1][0], data[1][1], '#000'), Point('p2', data[2][0], data[2][1]), '#000')
            
            self._ui.getCartesianPlane().canAddEntity(p) # to verify if this shape already exists in the plane
        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

    def defineMainLayout(self):
        self.createEntityForm(2)
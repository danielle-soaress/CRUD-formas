import resources_rc

from PyQt5.QtGui import QIcon
from package.UI.dialogues.Dialog import Dialog 
from package.maths.Point import Point
from package.maths.Line import *
from package.maths.Shapes import *
from package.exceptions.Exceptions import *
from package.UI.components.MessageBox import MessageBox
from package.UI.components.Inputs import *

class RectangleDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Rectangle information", QIcon(':/images/adicionar.png'))
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)

    def AreInputsValid(self):
        try:
            super().AreInputsValid()
            data = self.getData()
            rect = Rectangle(data[0], 
                    Point('Point 1', data[1][0], data[1][1]), 
                    Point('Point 2', data[2][0], data[2][1]), 
                    Point('Point 3', data[3][0], data[3][1]), 
                    Point('Point 4', data[4][0], data[4][1]), 
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
    
class TriangleDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Triangle information", QIcon(':/images/adicionar.png'))
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)

    def defineMainLayout(self):
        self.createEntityForm(3)

    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            data = self.getData()

            triangle = Triangle(data[0], 
                    Point('Point 1', data[1][0], data[1][1]), 
                    Point('Point 2', data[2][0], data[2][1]), 
                    Point('Point 3', data[3][0], data[3][1]), 
                    '#000')
            
            self._ui.getCartesianPlane().canAddEntity(triangle) # to verify if this shape already exists in the plane
        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

class CircleDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Circle information", QIcon(':/images/adicionar.png'))
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)

    def defineMainLayout(self):
        self.createEntityForm(0,True)

    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            data = self.getData()

            circle = Circle(data[0], 
                    Point('Point 1', data[1][0], data[1][1]), 
                    data[2],
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
        super().__init__(ui, "Insert Point information", QIcon(':/images/adicionar.png'))
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)

    def defineMainLayout(self):
        self.createEntityForm(1)

    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            data = self.getData()

            p = Point(data[0], data[1][0], data[1][1], '#000')
            
            self._ui.getCartesianPlane().canAddEntity(p) # to verify if this shape already exists in the plane
        except InvalidAction as b:
            MessageBox(self).showMessage('Error!', b.message)
            return False
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

class LineSegmentDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Line information", QIcon(':/images/adicionar.png'))
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
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

    def defineMainLayout(self):
        self.createEntityForm(2)

class LineDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Line information", QIcon(':/images/adicionar.png'))
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
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

    def defineMainLayout(self):
        self.createEntityForm(2)
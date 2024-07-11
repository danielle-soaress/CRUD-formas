from PyQt5.QtWidgets import QVBoxLayout, QDialogButtonBox
from package.UI.dialogues.Dialog import Dialog 
from package.UI.components.MessageBox import MessageBox
from package.maths.Point import Point
from package.maths.Shapes import Rectangle
from package.exceptions.Exceptions import InvalidAction

class RectangleDialog(Dialog):
    def __init__(self, ui):
        super().__init__(ui, "Insert Rectangle information")
        self.input_widgets = []

        # creating the main layout
        self.layout = QVBoxLayout()
        self.form_layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.defineMainLayout(4)
        self.setLayout(self.layout)

        # creating a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(lambda: self.accept() if self.AreInputsValid() else None)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def getData(self):
        return [
        self.input_widgets[0].text(),
        (self.input_widgets[1][0].value(), self.input_widgets[1][1].value()),
        (self.input_widgets[2][0].value(), self.input_widgets[2][1].value()),
        (self.input_widgets[3][0].value(), self.input_widgets[3][1].value()),
        (self.input_widgets[4][0].value(), self.input_widgets[4][1].value()),
        self.input_widgets[5].getCurrentColor()
        ]

    def AreInputsValid(self):
        if not self.AreInputsFilled(self.input_widgets):
            MessageBox(self).showMessage('Incomplete information!', 'You must fill all fields.')
            return False

        points = self.getData()[1:5] 

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
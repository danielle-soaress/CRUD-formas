import resources_rc

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QIcon
from package.UI.dialogues.Dialog import Dialog
from package.UI.components.MessageBox import MessageBox
from package.maths.Line import Line
from package.exceptions.Exceptions import *

class EntityActionDialog(Dialog):
    def __init__(self, ui, title, className, doubleForm = False, geometry = [300,300,300,100]):
        super().__init__(ui, title, QIcon(':/images/calculadora.png'), geometry)
        self.__cartesianPlane = self._ui.getCartesianPlane()
        self.__className = className
        self.__doubleForm = doubleForm
        
        quantityEntities = len(self.__cartesianPlane.getAllClassEntities(className))
        if (doubleForm == True and quantityEntities <2) or (doubleForm == False and quantityEntities == 0):
            MessageBox(self).showMessage('Error!', "There are not enough entities on the Cartesian plane to perform this operation.", "Please, create more entities and try again.")
            QTimer.singleShot(0, self.reject)

        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)


    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            if self.__doubleForm:
                data = self.getData()
                if data[0] == data[1]:
                    raise InvalidAction("You can't select the same entity.")

        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
    
    def defineMainLayout(self):
        options = self.__cartesianPlane.getAllClassEntities(self.__className)
        options = list(map(lambda x: x.getName(), options))

        self.comboBoxForm(options, 2 if self.__doubleForm else 1, True, labelText = f'Select a {self.__className.__name__}:')

class ShapesActionsDialog(Dialog):
    def __init__(self, ui, title, shapeClass, geometry = [300,300,250,100]):
        super().__init__(ui, title, QIcon(':/images/calculadora.png'), geometry)
        self.__cartesianPlane = self._ui.getCartesianPlane()
        self.__ShapeClass = shapeClass
        if len(self.__cartesianPlane.getAllClassEntities(shapeClass)) == 0:
            MessageBox(self).showMessage('Error!', "There are not enough entities on the Cartesian plane to perform this operation.", "Please, create more entities and try again.")
            QTimer.singleShot(0, self.reject)

        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)

    def AreInputsValid(self):
        try:
            super().AreInputsValid()

        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
    
    def defineMainLayout(self):
        options = self.__cartesianPlane.getAllClassEntities(self.__ShapeClass)
        options = list(map(lambda x: x.getName(), options))

        self.comboBoxForm(options, 1, True, 'Select the shape: ')

class EntitiesRelationship(Dialog):
    def __init__(self, ui, title, class1, class2, geometry = [300,300,250,100]):
        super().__init__(ui, title, QIcon(':/images/calculadora.png'), geometry)
        self.__cartesianPlane = self._ui.getCartesianPlane()
        self.__class1 = class1
        self.__class2 = class2

        if len(self.__cartesianPlane.getAllClassEntities(class1)) == 0 or len(self.__cartesianPlane.getAllClassEntities(class2)) == 0:
            MessageBox(self).showMessage('Error!', "There are not enough entities on the Cartesian plane to perform this operation.", "Please, create more entities and try again.")
            QTimer.singleShot(0, self.reject)

        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)

    def AreInputsValid(self):
        try:
            super().AreInputsValid()
            
        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
    
    def defineMainLayout(self):
        options1 = self.__cartesianPlane.getAllClassEntities(self.__class1)
        options1 = list(map(lambda x: x.getName(), options1))
        options2 = self.__cartesianPlane.getAllClassEntities(self.__class2)
        options2 = list(map(lambda x: x.getName(), options2))

        self.comboBoxForm2(options1, options2, [f'Select a {self.__class1.__name__}: ', f'Select a {self.__class2.__name__}: '])
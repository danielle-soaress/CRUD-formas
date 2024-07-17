from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QDialog, QVBoxLayout, QListWidget, QStackedLayout, QWidget, QComboBox
from PyQt5.QtCore import Qt, QTimer
from package.UI.dialogues.Dialog import Dialog
from package.UI.components.MessageBox import MessageBox
from package.UI.components.Inputs import PointInput
from package.maths.Point import Point
from package.exceptions.Exceptions import *

class PointActionsDialog(Dialog):
    def __init__(self, ui, title = 'Distance Between Two Points', geometry = [300,300,300,150]):
        super().__init__(ui, title, geometry)
        self.__cartesianPlane = self._ui.getCartesianPlane()
        
        if len(self.__cartesianPlane.getAllClassEntities(Point)) < 2:
            MessageBox(self).showMessage('Error!', "There are not enough points on the Cartesian plane to perform this operation.", "Please create more points and try again.")
            QTimer.singleShot(0, self.reject)

        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)


    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            data = self.getData()

            if data[0] == data[1]:
                raise InvalidAction("You can't select the same points.")

        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
    
    def defineMainLayout(self):
        self.form_layout = QVBoxLayout()
        # Criação de widgets para a opção "Escrever nome dos pontos"
        options = self.__cartesianPlane.getAllClassEntities(Point)
        options = list(map(lambda x: x.getName(), options))
        for i in range (0,2):
            label = QLabel(f"Ponto {i+1}: ")
            comboBox = QComboBox(self)
            comboBox.addItems(options)

            self.form_layout.addWidget(label)
            self.form_layout.addWidget(comboBox)
            self._input_widgets.append(comboBox)
        
        self.layout.addLayout(self.form_layout)

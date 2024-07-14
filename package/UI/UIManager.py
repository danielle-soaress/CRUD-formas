import sys
from PyQt5.QtWidgets import QApplication
from package.UI.UI import UI
from package.UI.dialogues.GeometricEntitiesDialogues import *
from PyQt5.QtWidgets import QDialog
from package.maths.Shapes import *
from package.maths.Point import Point
from package.maths.Line import *


class UIManager():
    def __init__(self, cartesianPlane):
        self.__cartesianPlane = cartesianPlane

    def run(self):
        app = QApplication(sys.argv)  # Cria a instância de QApplication
        self.__window = UI(900,600, self.__cartesianPlane)
        self.__window.show()  # Mostra a janela
        sys.exit(app.exec())

    
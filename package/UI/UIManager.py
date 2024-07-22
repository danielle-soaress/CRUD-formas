import sys
import resources_rc

from PyQt5.QtWidgets import QApplication
from package.UI.UI import UI
from package.UI.dialogues.GeometricEntitiesDialogues import *


class UIManager():
    def __init__(self, cartesianPlane):
        self.__cartesianPlane = cartesianPlane

    def run(self):
        app = QApplication(sys.argv)  # Cria a instância de QApplication
        self.__window = UI(900,600, self.__cartesianPlane)
        self.__window.show()  # Mostra a janela
        self.showStartupMessage()
        sys.exit(app.exec())

    def showStartupMessage(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowIcon(QIcon(':/images/icon.png'))
        msg.setWindowTitle("Cartesian Plane")
        msg.setText("Welcome!\n\n"
                    "Here are some tips and instructions for a better experience:\n\n"
                    "1. Due UI limitations, the program can only handle integer numbers for inputs.\n\n"
                    "2. Some entity functionalities will only work if the necessary quantity of objects are present on the Cartesian plane.\n\n"
                    "3. You can see some information about an entity by clicking on its name, spotted beside the entity's drawing, or by accessing the 'All Entities' menu.\n\n"
                    "4. Along the usage, there will be some other message boxes, like this one, to guide you and alert you about input errors.\n\n"
                    "5. The program was developed entirely in English, including its instructions, but the interface is simple and intuitive.\n\n"
                    "5. You can learn more by accessing the GitHub repository or reading the README.md file.\n\n")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    
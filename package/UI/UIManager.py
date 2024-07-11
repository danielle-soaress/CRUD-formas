import sys
from PyQt5.QtWidgets import QApplication
from package.UI.UI import UI

class UIManager():
    def __init__(self, cartesianPlane):
        self.__cartesianPlane = cartesianPlane

    def run(self):
        app = QApplication(sys.argv)  # Cria a instância de QApplication
        window = UI(900,600, self.__cartesianPlane)
        window.show()  # Mostra a janela
        sys.exit(app.exec())
    
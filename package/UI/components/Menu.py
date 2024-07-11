from PyQt5.QtWidgets import  QAction, QDialog
from PyQt5.QtGui import QIcon
<<<<<<< HEAD
from package.UI.dialogues.ShapesDialog import RectangleDialog
=======
from package.UI.dialogues.RectangleDialog import RectangleDialog
>>>>>>> 7c5d97ad7519b133910929f96041d8df5f8a9019
from package.maths.Shapes import Rectangle
from package.maths.Point import Point

class Menu():
    def __init__(self, UI):
        self.__ui = UI
        self.__menubar = UI.menuBar()

    def render(self):
        self.rectShapeMenu()
    
    def rectShapeMenu(self):
        rectmenu = self.__menubar.addMenu('&Rectangle')

        # to create a rect
<<<<<<< HEAD
=======

>>>>>>> 7c5d97ad7519b133910929f96041d8df5f8a9019
        createRectangle = QAction('&Create Rectangle', self.__ui)
        createRectangle.setShortcut('Alt+R')
        createRectangle.triggered.connect(lambda: self.drawRectangle())

        rectmenu.addAction(createRectangle)

    def drawRectangle(self):
        dialog = RectangleDialog(self.__ui)
        if dialog.exec_() == QDialog.Accepted:
            rect_data = dialog.getData()
            self.__ui.getCartesianPlane().addEntity(Rectangle(rect_data[0], 
                                                            Point(f'{rect_data[0]} - P1',rect_data[1][0], rect_data[1][1]), 
                                                            Point(f'{rect_data[0]} - P2', rect_data[2][0], rect_data[2][1]), 
                                                            Point(f'{rect_data[0]} - P3', rect_data[3][0], rect_data[3][1]), 
                                                            Point(f'{rect_data[0]} - P4', rect_data[4][0], rect_data[4][1]), 
                                                            rect_data[5]))
            print('Figura adicionada!')
            self.__ui.update()
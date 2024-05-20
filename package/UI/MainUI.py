import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QDesktopWidget, QApplication, QMenu, QAction, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QFormLayout
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor, QPolygon, QFontDatabase, QIcon, QBrush
from PyQt5.QtCore import Qt, QPoint, QRect


from package.UI.Dialogues import *
from package.maths.CartesianPlane import CartesianPlane
from package.maths.Shapes import *

class MainUI():
    def __init__(self):
        self.__cartesianPlane = CartesianPlane()

    def run(self):
        app = QApplication(sys.argv)  # Cria a instância de QApplication
        window = Window(900,600, self.__cartesianPlane)
        window.show()  # Mostra a janela
        sys.exit(app.exec())


class Window(QMainWindow):
    BACKGROUND_WHITE = '#f8f8f8'

    def __init__(self, width, height, cartesianPlane):
        super().__init__()
        self.__cartesianPlane = cartesianPlane

        self.setWindowTitle('Minha Janela PyQt')
        self.setGeometry(0, 0, width, height)  # Define o tamanho da janela
        self.centralize()  # Centraliza a janela
        self.setStyleSheet(f"background-color: {self.BACKGROUND_WHITE};")

        font_id = QFontDatabase.addApplicationFont('./font/itim.ttf')
        self.font = QFontDatabase.applicationFontFamilies(font_id)[0]
        
        self.renderMenu()

    def centralize(self):
        screen = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        screen.moveCenter(screen_center)
        self.move(screen.topLeft())

    def paintEvent(self, event):
        painter = QPainter(self)
        self.renderMainElements(painter)

        for shape in self.__cartesianPlane.getShapes():
            print(shape)
            painter.setBrush(QBrush(QColor(shape.getFillColor())))
            if isinstance(shape, Rectangle):
                rect = QRect(shape.getX(), shape.getY(), shape.getWidth(), shape.getHeight())
                painter.drawRect(rect)

    def renderMainElements(self, painter):
        painter.setRenderHint(QPainter.Antialiasing) # configurando o estilo de renderização

        pen = QPen (QColor("#C1C1C1"), 1, Qt.SolidLine)
        painter.setPen(pen)

        # Desenha as linhas da grade ao longo do eixo x
        for x in range(0, self.width(), 20):
            painter.drawLine(x, 0, x, self.height())

        # Desenha as linhas da grade ao longo do eixo y
        for y in range(0, self.height(), 20):
            painter.drawLine(0, y, self.width(), y)


        pen = QPen (Qt.black, 4, Qt.SolidLine)
        painter.setPen(pen)
        painter.setBrush(Qt.black)

        # x axis
        painter.drawLine(0, self.height()-40, self.width() - 10, self.height()-40)
        xArrow = QPolygon([
            QPoint(self.width()-10, self.height()-40-5),
            QPoint(self.width()-10, self.height()-40+5),
            QPoint(self.width(), self.height()-40)
        ])
        painter.drawPolygon(xArrow)

        # y axis
        painter.drawLine(40,10, 40, self.height())
        yArrow = QPolygon([
            QPoint(40,0),
            QPoint(40-5, 10),
            QPoint(40+5, 10)
        ])
        painter.drawPolygon(yArrow)

        # marcadores 

        for x in range(0, self.width(), 20):
            if x % 40 == 0 and x != 40:
                painter.drawText(x -5, self.height() - 25, str((x - 40) // 20))

        for y in range(0, self.height(), 20):
            if y % 40 == 0 and y != 40:
                painter.drawText(20, self.height() - y+5, str((y - 40) // 20))

    def renderMenu(self):
        menubar = self.menuBar()

        self.newShapeActions(menubar)

    def newShapeActions(self, menubar):
        newShape = menubar.addMenu('&New Shape')

        # to create a rect

        createRectangle = QAction('&Create Rectangle', self)
        createRectangle.setShortcut('Alt+R')
        createRectangle.setIcon(QIcon('./images/rect_icon.png'))
        createRectangle.triggered.connect(lambda: self.drawRectangle())

        newShape.addAction(createRectangle)
    
    def open_rectangle_dialog(self):
        dialog = RectangleDialog()
        if dialog.exec_() == QDialog.Accepted:
            rect_data = dialog.get_data()
            self.update()

    def drawRectangle(self):
        self.__cartesianPlane.addShape(Rectangle(123,300,300,50,100, '#000'))
        self.update()
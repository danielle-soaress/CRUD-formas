import sys
from PyQt5.QtWidgets import QMainWindow,  QDesktopWidget, QApplication, QAction, QDialog
from PyQt5.QtGui import QPainter, QPen, QColor, QPolygon, QFontDatabase, QIcon, QBrush
from PyQt5.QtCore import Qt, QPoint, QRect


from package.UI.Dialogues import *
from package.maths.CartesianPlane import CartesianPlane
from package.maths.Shapes import *
from package.maths.Point import Point

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

    def getCartesianPlane(self): # to access the cartesian plane associated with the window from outside the class
        return self.__cartesianPlane

    def centralize(self): # to centralize the window on the user's screen, independently of screen size 
        screen = self.frameGeometry()
        screen_center = QDesktopWidget().availableGeometry().center()
        screen.moveCenter(screen_center)
        self.move(screen.topLeft())

    def paintEvent(self, event): # this function is responsible for render the figures and other paints
        painter = QPainter(self)
        self.renderMainElements(painter)

        pen = QPen(QColor('#000'))
        pen.setWidth(2)
        painter.setPen(pen)
        
        # the calculation to draw the figures consider the following facts:
        # 1. the values inserted by user aren't converted yet.
        # 2. there are spaces of 40px from window borders to axis lines
        # 3. each side of grid squares has 20px.
        # so, the calculation is: 40+20*(value inserted by user)
        # to do this, we'll use the "convert" function
        
        for shape in self.__cartesianPlane.getShapes():
            painter.setBrush(QBrush(QColor(shape.getFillColor())))
        
            if isinstance(shape, Rectangle):
                rect = QRect(self.convertValue(shape.getAPoint(1).getCoordX()), 
                             self.height() - self.convertValue(shape.getAPoint(1).getCoordY()), 20*shape.getWidth(),
                             20*shape.getHeight())
                painter.drawRect(rect)
            elif isinstance(shape, Triangule):
                triangule = QPolygon([
                    QPoint(self.convertValue(shape.getAPoint(0).getCoordX()), self.height() - self.convertValue(shape.getAPoint(0).getCoordY())),
                    QPoint(self.convertValue(shape.getAPoint(1).getCoordX()), self.height() - self.convertValue(shape.getAPoint(1).getCoordY())),
                    QPoint(self.convertValue(shape.getAPoint(2).getCoordX()), self.height() - self.convertValue(shape.getAPoint(2).getCoordY()))
                ])

                painter.drawPolygon(triangule)
            elif isinstance(shape, Point):
                point = QPoint(self.convertValue(shape.getCoordX()), self.height() - self.convertValue((shape.getCoordY())))
                painter.drawEllipse(point, 4, 4)


    def renderMainElements(self, painter): # this function is responsible for render the grid, x and y axis and their markers.
        painter.setRenderHint(QPainter.Antialiasing) # configurando o estilo de renderização

        pen = QPen (QColor("#C1C1C1"), 1, Qt.SolidLine)
        painter.setPen(pen)

        # desenha as linhas da grade ao longo do eixo x
        for x in range(0, self.width(), 20):
            painter.drawLine(x, 0, x, self.height())

        # desenha as linhas da grade ao longo do eixo y
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

    def renderMenu(self): # this function is responsible for render the menu and connect it to the window
        menubar = self.menuBar()

        self.newShapeActions(menubar)
        self.myShapesActions(menubar)

    def newShapeActions(self, menubar): # from here down, I'll probabily encapsulate into a new class called Menu
        newShape = menubar.addMenu('&New Shape')

        # to create a rect

        createRectangle = QAction('&Create Rectangle', self)
        createRectangle.setShortcut('Alt+R')
        createRectangle.setIcon(QIcon('./images/rect_icon.png'))
        createRectangle.triggered.connect(lambda: self.drawRectangle())

        newShape.addAction(createRectangle)

        # to create a triangule
        
        createPoint = QAction('&Create Triangule', self)
        createPoint.setShortcut('Alt+T')
        createPoint.setIcon(QIcon('./images/rect_icon.png'))
        createPoint.triggered.connect(lambda: self.drawTriangule())

        newShape.addAction(createPoint)

        # to create a point
        
        createPoint = QAction('&Create Point', self)
        createPoint.setShortcut('Alt+P')
        createPoint.setIcon(QIcon('./images/rect_icon.png'))
        createPoint.triggered.connect(lambda: self.drawPoint())

        newShape.addAction(createPoint)
    
    def myShapesActions(self, menubar):
        myShapes = menubar.addMenu('&My Shapes')

        # see all shapes information
        shapesInformation = QAction('&Manage my shapes', self)
        shapesInformation.setShortcut('Alt+M')
        shapesInformation.setIcon(QIcon('./images/rect_icon.png'))
        shapesInformation.triggered.connect(lambda: ShapesInformation(self, self.__cartesianPlane).open())
        myShapes.addAction(shapesInformation)
        
        # delete all shapes ----------- I still need to do this...

    def drawRectangle(self):
        dialog = RectangleDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            rect_data = dialog.getData()
            self.__cartesianPlane.addShape(Rectangle(rect_data[0], 
                                                     Point(f'{rect_data[0]} - P1',rect_data[1][0], rect_data[1][1]), 
                                                     Point(f'{rect_data[0]} - P2', rect_data[2][0], rect_data[2][1]), 
                                                     Point(f'{rect_data[0]} - P3', rect_data[3][0], rect_data[3][1]), 
                                                     Point(f'{rect_data[0]} - P4', rect_data[4][0], rect_data[4][1]), 
                                                     rect_data[5]))
            self.update()

    def drawPoint(self):
        dialog = PointDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            point_data = dialog.getData()
            self.__cartesianPlane.addShape(Point(point_data[0], point_data[1][0], point_data[1][1], point_data[2]))
            self.update()

    def drawTriangule(self):
        dialog = TrianguleDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            triangule_data = dialog.getData()
            self.__cartesianPlane.addShape(Triangule(triangule_data[0], 
                                                     Point(f'{triangule_data[0]} - P1',triangule_data[1][0], triangule_data[1][1]), 
                                                     Point(f'{triangule_data[0]} - P2', triangule_data[2][0], triangule_data[2][1]), 
                                                     Point(f'{triangule_data[0]} - P3', triangule_data[3][0], triangule_data[3][1]), 
                                                     triangule_data[4]))
            self.update()

    def convertValue(self, value): # this function is 
        return 40+20*value

        
import sys
from PyQt5.QtWidgets import QMainWindow,  QDesktopWidget, QApplication, QAction, QDialog
from PyQt5.QtGui import QPainter, QPen, QColor, QPolygon, QFontDatabase, QIcon, QBrush, QFont
from PyQt5.QtCore import Qt, QPoint, QRect, QLineF, QPointF


from package.UI.Dialogues import *
from package.maths.CartesianPlane import CartesianPlane
from package.maths.Shape import Shape
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
        
        for figure in self.__cartesianPlane.getFigures():
            painter.setBrush(QBrush(QColor(figure.getFillColor())))
            if isinstance(figure, Shape):
                if isinstance(figure, Rectangle):
                    rect = QRect(self.convertValue(figure.getAPoint(1).getCoordX()), 
                                self.height() - self.convertValue(figure.getAPoint(1).getCoordY()), 20*figure.getWidth(),
                                20*figure.getHeight())
                    painter.drawRect(rect)
                elif isinstance(figure, Triangule):
                    triangule = QPolygon([
                        QPoint(self.convertValue(figure.getAPoint(0).getCoordX()), self.height() - self.convertValue(figure.getAPoint(0).getCoordY())),
                        QPoint(self.convertValue(figure.getAPoint(1).getCoordX()), self.height() - self.convertValue(figure.getAPoint(1).getCoordY())),
                        QPoint(self.convertValue(figure.getAPoint(2).getCoordX()), self.height() - self.convertValue(figure.getAPoint(2).getCoordY()))
                    ])
                    painter.drawPolygon(triangule)
                elif isinstance(figure, Circle):
                    radius = 20*figure.getRadius()
                    painter.drawEllipse(self.convertValue(figure.getAPoint(0).getCoordX()) - radius, self.height() - radius - self.convertValue(figure.getAPoint(0).getCoordY()), 2*radius, 2*radius)
            elif isinstance(figure, Point):
                point = QPoint(self.convertValue(figure.getCoordX()), self.height() - self.convertValue((figure.getCoordY())))
                painter.drawEllipse(point, 4, 4)
            elif isinstance(figure, Line):
                point1 = QPointF(self.convertValue(figure.getPoint1().getCoordX()), self.height() - self.convertValue(figure.getPoint1().getCoordY()))
                point2 = QPointF(self.convertValue(figure.getPoint2().getCoordX()), self.height() - self.convertValue(figure.getPoint2().getCoordY()))
            
                # calculate the line that pass through the two points 
                line = QLineF(point1, point2)

                # maximum line extension beyond the window limits
                length = max(self.width(), self.height())  
                infinite_line = QLineF()
                infinite_line.setP1(line.pointAt(-length))
                infinite_line.setP2(line.pointAt(2 * length))

                painter.setBrush(QBrush(QColor('#000')))
                painter.drawLine(infinite_line)

                # draw the points
                painter.setBrush(QBrush(QColor(figure.getFillColor())))
                painter.drawEllipse(point1, 4, 4)
                painter.drawEllipse(point2, 4, 4)

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

        self.myFiguresMenu(menubar)
        self.newShapeMenu(menubar)
        self.pointMenu(menubar)
        self.lineMenu(menubar)

    def newShapeMenu(self, menubar): # from here down, I'll probabily encapsulate into a new class called Menu
        newShape = menubar.addMenu('&New Shape')

        # to create a rect

        createCircle = QAction('&Create Circle', self)
        createCircle.setShortcut('Alt+R')
        createCircle.setIcon(QIcon('./images/rect_icon.png'))
        createCircle.triggered.connect(lambda: self.drawCircle())

        newShape.addAction(createCircle)

        # to create a rect

        createRectangle = QAction('&Create Rectangle', self)
        createRectangle.setShortcut('Alt+R')
        createRectangle.setIcon(QIcon('./images/rect_icon.png'))
        createRectangle.triggered.connect(lambda: self.drawRectangle())

        newShape.addAction(createRectangle)

        # to create a triangule
        
        createTriangule = QAction('&Create Triangule', self)
        createTriangule.setShortcut('Alt+T')
        createTriangule.setIcon(QIcon('./images/rect_icon.png'))
        createTriangule.triggered.connect(lambda: self.drawTriangule())

        newShape.addAction(createTriangule)
    
    def myFiguresMenu(self, menubar):
        myFigures = menubar.addMenu('&My figures')

        # see all shapes information
        figuresInformation = QAction('&Manage my figures', self)
        figuresInformation.setShortcut('Alt+M')
        figuresInformation.setIcon(QIcon('./images/rect_icon.png'))
        figuresInformation.triggered.connect(lambda: FiguresInformation(self, self.__cartesianPlane).open())
        myFigures.addAction(figuresInformation)
        
        # delete all shapes 
        deleteFigures = QAction('&Delete all figures', self)
        deleteFigures.setShortcut('Alt+D')
        deleteFigures.setIcon(QIcon('./images/rect_icon.png'))
        deleteFigures.triggered.connect(lambda: DeleteFigures(self, self.__cartesianPlane).open())
        myFigures.addAction(deleteFigures)

    def pointMenu(self, menubar):
        pointMenu = menubar.addMenu('&Point')

        # to insert a point
        insertPoint = QAction('&Create Point', self)
        insertPoint.setShortcut('Alt+P')
        insertPoint.setIcon(QIcon('./images/rect_icon.png'))
        insertPoint.triggered.connect(lambda: self.drawPoint())

        pointMenu.addAction(insertPoint)
        
        # distance between two points
        distanceBetween = QAction('&Distance Between 2 Points', self)
        distanceBetween.setShortcut('Alt+1')
        distanceBetween.setIcon(QIcon('./images/rect_icon.png'))
        distanceBetween.triggered.connect(lambda: self.pointActions('distancePoints', 'Distance Between Two Points'))
        pointMenu.addAction(distanceBetween)

        # median between two points

        medianBetween = QAction('&Median', self)
        medianBetween.setShortcut('Alt+2')
        medianBetween.setIcon(QIcon('./images/rect_icon.png'))
        medianBetween.triggered.connect(lambda: self.pointActions('median', 'Median Between Two Points'))
        pointMenu.addAction(medianBetween)

        # distance from origin

        distanceOrigin = QAction('&Distance From Origin', self)
        distanceOrigin.setShortcut('Alt+3')
        distanceOrigin.setIcon(QIcon('./images/rect_icon.png'))
        distanceOrigin.triggered.connect(lambda: self.pointActions('distanceOrigin', 'Distance From Origin'))
        pointMenu.addAction(distanceOrigin)

    def pointActions(self, action, nameAction):
        dialog = PointActionsDialog(action, self, nameAction)

        if dialog.exec_() == QDialog.Accepted:
            data = dialog.getData()

            result = None
            try:
                if action == "distanceOrigin":
                    p = None
                    if data[0] == 'names':
                        p = self.__cartesianPlane.getAFigureByName(data[1])
                    else:
                        p = Point('point', data[1][0], data[1][1])
                    
                    result = f'The distance of the point from origin is: {p.distanceFromOrigin()}'
                else:
                    p1 = None
                    p2 = None
                    if data[0] == 'names':
                        p1 = self.__cartesianPlane.getAFigureByName(data[1])
                        p2 = self.__cartesianPlane.getAFigureByName(data[2])
                    else:
                        p1 = Point('point', data[1][0], data[1][1])
                        p2 = Point('point', data[2][0], data[2][1])
                    
                    if action == "median":
                        result = f'The median between the points is: {p1.medianBetween(p2)}'
                    else:
                        result = f'The distance between the points is: {p1.distanceTo(p2)}'

                MessageBox(self).showMessage('Operation Result', result, '', QMessageBox.Information)
                self.update()
            except InvalidShape as e:
                MessageBox(self).showMessage('Error!', 'Something is wrong...', e.message, QMessageBox.Critical)

    def lineMenu(self, menubar):
        pointMenu = menubar.addMenu('&Line')

        # to insert a line
        insertPoint = QAction('&Create Line', self)
        insertPoint.setShortcut('Alt+L')
        insertPoint.setIcon(QIcon('./images/rect_icon.png'))
        insertPoint.triggered.connect(lambda: self.drawLine())

        pointMenu.addAction(insertPoint)
        
    def drawRectangle(self):
        dialog = RectangleDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            rect_data = dialog.getData()
            self.__cartesianPlane.addFigure(Rectangle(rect_data[0], 
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
            self.__cartesianPlane.addFigure(Point(point_data[0], point_data[1][0], point_data[1][1], point_data[2]))
            self.update()

    def drawTriangule(self):
        dialog = TrianguleDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            triangule_data = dialog.getData()
            self.__cartesianPlane.addFigure(Triangule(triangule_data[0], 
                                                     Point(f'{triangule_data[0]} - P1',triangule_data[1][0], triangule_data[1][1]), 
                                                     Point(f'{triangule_data[0]} - P2', triangule_data[2][0], triangule_data[2][1]), 
                                                     Point(f'{triangule_data[0]} - P3', triangule_data[3][0], triangule_data[3][1]), 
                                                     triangule_data[4]))
            self.update()

    def drawCircle(self):
        dialog = CircleDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            circle_data = dialog.getData()
            self.__cartesianPlane.addFigure(Circle(circle_data[0], 
                                                    Point(f'{circle_data[0]} - P1',circle_data[1][0], circle_data[1][1]), 
                                                    circle_data[2],
                                                    circle_data[3]))
            self.update()

    def drawLine(self):
        dialog = LineDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            line_data = dialog.getData()
            self.__cartesianPlane.addFigure(Line(line_data[0], 
                                                Point(f'{line_data[0]} - P1',line_data[1][0], line_data[1][1]), 
                                                Point(f'{line_data[0]} - P1',line_data[2][0], line_data[2][1]), 
                                                line_data[3]))
            self.update()

    def convertValue(self, value):  # this function is used to calculate the real value of each measurements.
        return 40+20*value          # - consider that the distances between the axis and window borders must be disregarded
                                    # each grid square is 20px x 20px
        
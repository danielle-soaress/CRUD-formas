import resources_rc

from PyQt5.QtWidgets import QMainWindow,  QDesktopWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QPolygon, QBrush, QIcon
from PyQt5.QtCore import Qt, QPoint, QRect, QPointF, QLineF, QRectF, QSizeF

from package.UI.components.Menu import Menu
from package.UI.dialogues.InformativeDialogues import FigureInfoDialog
from package.maths.Shape import Shape
from package.maths.Shapes import *
from package.maths.Point import Point
from package.maths.Line import *


##
##
## The UI Class is not fully developed. At the moment, only the 'draw Rectangle' function was disponibilized for User.
##
##

class UI(QMainWindow):
    BACKGROUND_WHITE = '#f8f8f8'

    def __init__(self, width, height, cartesianPlane):
        super().__init__()

        self.__cartesianPlane = cartesianPlane

        self.setWindowTitle('Cartesian Plane')
        self.setWindowIcon(QIcon(':/images/icon.png'))
        self.setFixedSize(width, height)
        self.centralize()
        self.setStyleSheet(f"background-color: {self.BACKGROUND_WHITE};")

        self.__menu = Menu(self)
        self.__menu.render()

        self.figure_texts = []
        self.setMouseTracking(True)

    def getCartesianPlane(self):
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

        self.figure_texts = []

        # the calculation to draw the figures consider the following facts:
        # 1. the values inserted by user aren't converted yet.
        # 2. there are spaces of 40px from window borders to axis lines
        # 3. each side of grid squares has 20px.
        # so, the calculation is: 40+20*(value inserted by user)
        # to do this, we'll use the "convert" function
        
        for figure in self.__cartesianPlane.getEntities():
            painter.setBrush(QBrush(QColor(figure.getFillColor())))
            if isinstance(figure, Shape):
                if isinstance(figure, Rectangle):
                    rect = QRect(self.convertValue(figure.getAPoint(1).getCoordX()), 
                                self.height() - self.convertValue(figure.getAPoint(1).getCoordY()), 20*figure.width(),
                                20*figure.height())
                    painter.drawRect(rect)

                    text_position = rect.topRight() + QPointF(10, -10)
                elif isinstance(figure, Triangle):
                    points = [
                        QPoint(self.convertValue(figure.getAPoint(0).getCoordX()), self.height() - self.convertValue(figure.getAPoint(0).getCoordY())),
                        QPoint(self.convertValue(figure.getAPoint(1).getCoordX()), self.height() - self.convertValue(figure.getAPoint(1).getCoordY())),
                        QPoint(self.convertValue(figure.getAPoint(2).getCoordX()), self.height() - self.convertValue(figure.getAPoint(2).getCoordY()))
                    ]
                    triangle = QPolygon(points)
                    painter.drawPolygon(triangle)

                    rightmost_point = max(points, key=lambda p: p.x())
                    text_position = QPointF(rightmost_point.x() + 10, rightmost_point.y() - 10)

                elif isinstance(figure, Circle):
                    radius = 20*figure.getRadius()
                    painter.drawEllipse(self.convertValue(figure.getAPoint(0).getCoordX()) - radius, self.height() - radius - self.convertValue(figure.getAPoint(0).getCoordY()), 2*radius, 2*radius)
                    text_position = QPointF(self.convertValue(figure.getAPoint(0).getCoordX()) + radius + 2, self.height() - self.convertValue(figure.getAPoint(0).getCoordY()) - radius - 2)
            elif isinstance(figure, Point):
                point = QPoint(self.convertValue(figure.getCoordX()), self.height() - self.convertValue((figure.getCoordY())))
                painter.drawEllipse(point, 4, 4)
                text_position = point + QPointF(15, -20)
            elif isinstance(figure, LineSegment):
                point1 = QPointF(self.convertValue(figure.getPoint1().getCoordX()), self.height() - self.convertValue(figure.getPoint1().getCoordY()))
                point2 = QPointF(self.convertValue(figure.getPoint2().getCoordX()), self.height() - self.convertValue(figure.getPoint2().getCoordY()))
            
                # calculate the line that pass through the two points 
                line = QLineF(point1, point2)
                painter.drawLine(line)

                # draw the points
                painter.setBrush(QBrush(QColor(figure.getFillColor())))
                painter.drawEllipse(point1, 4, 4)
                painter.drawEllipse(point2, 4, 4)
                text_position = (point1 + point2) / 2 + QPointF(5, -5)
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
                text_position = (point1 + point2) / 2 + QPointF(5, -5)

            text_rect = QRectF(text_position, QSizeF(50, 20))  # Adjust size as needed
            self.figure_texts.append((text_rect, figure))
            painter.drawText(text_rect, Qt.AlignLeft, figure.getName())

    def mouseMoveEvent(self, event):
        for text_rect, _ in self.figure_texts:
            if text_rect.contains(event.pos()):
                self.setCursor(Qt.PointingHandCursor)
                return
        self.setCursor(Qt.ArrowCursor)

    def mousePressEvent(self, event):
        for text_rect, figure in self.figure_texts:
            if text_rect.contains(event.pos()):
                dialog = FigureInfoDialog(figure, self)
                dialog.exec_()
                self.update()  # Redraw to update any changes in figure info
                break

    def renderMainElements(self, painter):  # to render the grid and axes and their markers.

        painter.setRenderHint(QPainter.Antialiasing)

        # grid
        pen = QPen(QColor("#C1C1C1"), 1, Qt.SolidLine)
        painter.setPen(pen)
        for x in range(0, self.width(), 20):
            painter.drawLine(x, 0, x, self.height())

        for y in range(0, self.height(), 20):
            painter.drawLine(0, y, self.width(), y)

        # x axis
        pen = QPen(Qt.black, 4, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(0, self.height()-40, self.width() - 10, self.height()-40)

        # x axis arrow
        painter.setBrush(Qt.black)
        xArrow = QPolygon([
            QPoint(self.width()-10, self.height()-40-5),
            QPoint(self.width()-10, self.height()-40+5),
            QPoint(self.width(), self.height()-40)
        ])
        painter.drawPolygon(xArrow)

        # y axis
        painter.drawLine(40, 10, 40, self.height())

        # y axis arrow
        yArrow = QPolygon([
            QPoint(40, 0),
            QPoint(40-5, 10),
            QPoint(40+5, 10)
        ])
        painter.drawPolygon(yArrow)

        # axes markers
        for x in range(0, self.width(), 20):
            if x % 40 == 0 and x != 40:
                painter.drawText(x - 5, self.height() - 25, str((x - 40) // 20))

        for y in range(0, self.height(), 20):
            if y % 40 == 0 and y != 40:
                painter.drawText(20, self.height() - y + 5, str((y - 40) // 20))

    def convertValue(self, value):  # this function is used to calculate the real value of each measurements.
        return 40+20*value          # - consider that the distances between the axis and window borders must be disregarded
                                    # each grid square is 20px x 20px
    
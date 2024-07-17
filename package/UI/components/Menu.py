from PyQt5.QtWidgets import  QAction, QDialog
from PyQt5.QtGui import QIcon
from package.UI.dialogues.GeometricEntitiesDialogues import *
from package.maths.Shapes import *
from package.maths.Line import *
from package.maths.Point import Point
from package.UI.dialogues.InformativeDialogues import *
from package.UI.dialogues.PointFunctionsDialogues import *

class Menu():
    def __init__(self, UI):
        self.__ui = UI
        self.__menubar = UI.menuBar()


    def render(self):
        self.Entities()
        self.rectMenu()
        self.trianguleMenu()
        self.circleMenu()
        self.pointMenu()
        self.lineMenu()

    def rectMenu(self):
        rectmenu = self.__menubar.addMenu('&Rectangle')

        # to create a rect
        createRectangle = QAction('&Create Rectangle', self.__ui)
        createRectangle.setShortcut('Alt+1')
        createRectangle.triggered.connect(lambda: self.drawEntity('rect'))

        rectmenu.addAction(createRectangle)
    
    def trianguleMenu(self):
        trianguleMenu = self.__menubar.addMenu('&Triangule')

        # to create a triangule   
        createTriangule = QAction('&Create Triangule', self.__ui)
        createTriangule.setShortcut('Alt+2')
        createTriangule.triggered.connect(lambda: self.drawEntity('triangule'))

        trianguleMenu.addAction(createTriangule)
    
    def circleMenu(self):
        circleMenu = self.__menubar.addMenu('&Circle')

        # to create a circle   
        createCircle = QAction('&Create Circle', self.__ui)
        createCircle.setShortcut('Alt+3')
        createCircle.triggered.connect(lambda: self.drawEntity('circle'))

        circleMenu.addAction(createCircle)
    
    def pointMenu(self):
        pMenu = self.__menubar.addMenu('&Point')

        # to create a Point   
        createPoint = QAction('&Create Point', self.__ui)
        createPoint.setShortcut('Alt+4')
        createPoint.triggered.connect(lambda: self.drawEntity('point'))

        pMenu.addAction(createPoint)

        # relation between 2 points
        distanceBetween = QAction('&Distance between two points', self.__ui)
        distanceBetween.setShortcut('Shift+D')
        distanceBetween.triggered.connect(lambda: None)
        distanceBetween.triggered.connect(lambda: self.pointActions('distanceBetween'))

        pMenu.addAction(distanceBetween)

        # relation between 2 points
        medianBetween = QAction('&Median between two points', self.__ui)
        medianBetween.setShortcut('Shift+D')
        medianBetween.triggered.connect(lambda: None)
        medianBetween.triggered.connect(lambda: self.pointActions('medianBetween'))

        pMenu.addAction(medianBetween)
    
    def lineMenu(self):
        lineMenu = self.__menubar.addMenu('&Line')

        # to create a Line   
        createLine = QAction('&Create Line', self.__ui)
        createLine.setShortcut('Alt+5')
        createLine.triggered.connect(lambda: self.drawEntity('line'))
        lineMenu.addAction(createLine)
        # to create a Line Segment 
        createLineSegment = QAction('&Create Line Segment', self.__ui)
        createLineSegment.setShortcut('Alt+6')
        createLineSegment.triggered.connect(lambda: self.drawEntity('lineSegment'))

        lineMenu.addAction(createLineSegment)

    def Entities(self):
        entitiesMenu = self.__menubar.addMenu('&All Entities')

        # to create a triangule   
        manageEntities = QAction('&Manage Entities', self.__ui)
        manageEntities.setShortcut('Alt+0')
        manageEntities.triggered.connect(lambda: AllFiguresInformation(self.__ui, "Manage Entities").open())
        entitiesMenu.addAction(manageEntities)

        # to create a triangule   
        deleteEntities = QAction('&Delete All Entities', self.__ui)
        deleteEntities.setShortcut('Alt+D')
        deleteEntities.triggered.connect(lambda: DeleteEntities(self.__ui, "Delete All Entities").open())
        entitiesMenu.addAction(deleteEntities)

    def drawEntity(self, type):
        if type == 'rect':
            dialog = RectangleDialog(self.__ui)
            if dialog.exec_() == QDialog.Accepted:
                rect_data = dialog.getData()
                self.__ui.getCartesianPlane().addEntity(Rectangle(rect_data[0], 
                                                                Point('Point 1',rect_data[1][0], rect_data[1][1]), 
                                                                Point('Point 2', rect_data[2][0], rect_data[2][1]), 
                                                                Point('Point 3', rect_data[3][0], rect_data[3][1]), 
                                                                Point('Point 4', rect_data[4][0], rect_data[4][1]), 
                                                                rect_data[5]))
        elif type == 'triangule':
            dialog = TrianguleDialog(self.__ui)
            if dialog.exec_() == QDialog.Accepted:
                triang_data = dialog.getData()
                self.__ui.getCartesianPlane().addEntity(Triangule(triang_data[0], 
                                                                Point('Point 1',triang_data[1][0], triang_data[1][1]), 
                                                                Point('Point 2', triang_data[2][0], triang_data[2][1]), 
                                                                Point('Point 3', triang_data[3][0], triang_data[3][1]), 
                                                                triang_data[4]))
        elif type == 'circle':
            dialog = CircleDialog(self.__ui)
            if dialog.exec_() == QDialog.Accepted:
                circle_data = dialog.getData()
                self.__ui.getCartesianPlane().addEntity(Circle(f'{circle_data[0]}',
                                                        Point('Central Point', circle_data[1][0], circle_data[1][1]), 
                                                        circle_data[2],
                                                        circle_data[3],
                                                        ))
        elif type == 'point':
            dialog = PointDialog(self.__ui)
            if dialog.exec_() == QDialog.Accepted:
                point_data = dialog.getData()
                self.__ui.getCartesianPlane().addEntity(Point(point_data[0], point_data[1][0], point_data[1][1], point_data[2]))
        elif type == 'line':
            dialog = LineDialog(self.__ui)
            if dialog.exec_() == QDialog.Accepted:
                line_data = dialog.getData()
                self.__ui.getCartesianPlane().addEntity(Line(line_data[0], 
                                                            Point('Point 1',line_data[1][0], line_data[1][1]), 
                                                            Point('Point 2', line_data[2][0], line_data[2][1]), 
                                                            line_data[3]))
        elif type == 'lineSegment':
            dialog = LineSegmentDialog(self.__ui)
            if dialog.exec_() == QDialog.Accepted:
                line_data = dialog.getData()
                self.__ui.getCartesianPlane().addEntity(LineSegment(line_data[0], 
                                                                    Point('Point 1',line_data[1][0], line_data[1][1]), 
                                                                    Point('Point 2', line_data[2][0], line_data[2][1]), 
                                                                    line_data[3]))
        
        self.__ui.update()

    def pointActions(self, action):
        plane = self.__ui.getCartesianPlane()
        if action == 'distanceBetween':
            dialog = PointActionsDialog(self.__ui)
            if dialog.exec_() == QDialog.Accepted:
                data = dialog.getData()
                p1 = self.__ui.getCartesianPlane().getAEntitieByName(data[0])
                p2 = self.__ui.getCartesianPlane().getAEntitieByName(data[1])
                result = p1.distanceTo(p2)

                OperationResult(self.__ui, 
                                f'The result of "Distance Between Two Points" operation is: <b>{result:2f}</b>'
                                ).open()
        if action == 'medianBetween':
            dialog = PointActionsDialog(self.__ui)
            if dialog.exec_() == QDialog.Accepted:
                data = dialog.getData()
                p1 = self.__ui.getCartesianPlane().getAEntitieByName(data[0])
                p2 = self.__ui.getCartesianPlane().getAEntitieByName(data[1])
                result = p1.medianBetween(p2)

                OperationResult(self.__ui, 
                                f'The result of "Median Between Two Points" operation is: <b>{result}</b>'
                                ).open()

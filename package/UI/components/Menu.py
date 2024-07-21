from PyQt5.QtWidgets import  QAction, QDialog
from package.UI.dialogues.GeometricEntitiesDialogues import *
from package.maths.Shapes import *
from package.maths.Line import *
from package.maths.Point import Point
from package.UI.dialogues.InformativeDialogues import *
from package.UI.dialogues.ActionsDialog import *

class Menu():
    def __init__(self, UI):
        self.__ui = UI
        self.__menubar = UI.menuBar()

    def render(self):
        self.EntitiesMenu()
        self.rectMenu()
        self.TriangleMenu()
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

        # calculate area and perimeter
        areaPerimeterAction = QAction('&Area and Perimeter', self.__ui)
        areaPerimeterAction.setShortcut('')
        areaPerimeterAction.triggered.connect(lambda: self.entitiesActions('areaPerimeter', "Area and Perimeter", Rectangle))
        rectmenu.addAction(areaPerimeterAction)

        # calculate width and height
        widthAndHeightAction = QAction('&Width and Height', self.__ui)
        widthAndHeightAction.setShortcut('')
        widthAndHeightAction.triggered.connect(lambda: self.entitiesActions('widthHeight', "Width and Height", Rectangle))
        rectmenu.addAction(widthAndHeightAction)

    def TriangleMenu(self):
        TriangleMenu = self.__menubar.addMenu('&Triangle')

        # to create a Triangle   
        createTriangle = QAction('&Create Triangle', self.__ui)
        createTriangle.setShortcut('Alt+2')
        createTriangle.triggered.connect(lambda: self.drawEntity('Triangle'))
        TriangleMenu.addAction(createTriangle)
        
        # to get area and perimeter information 
        areaPerimeterAction = QAction('&Area and Perimeter', self.__ui)
        areaPerimeterAction.setShortcut('')
        areaPerimeterAction.triggered.connect(lambda: self.entitiesActions('areaPerimeter', 'Area and Perimeter', Triangle))
        TriangleMenu.addAction(areaPerimeterAction)

        # to get angles and sides information 
        anglesAndSidesAction = QAction('&Angles and Sides', self.__ui)
        anglesAndSidesAction.setShortcut('')
        anglesAndSidesAction.triggered.connect(lambda: self.entitiesActions('anglesSides', 'Angles and Sides', Triangle))
        TriangleMenu.addAction(anglesAndSidesAction)

        # to get classification information
        classificationAction = QAction('&Triangle Classification', self.__ui)
        classificationAction.setShortcut('')
        classificationAction.triggered.connect(lambda: self.entitiesActions('classify', 'Triangle Classification', Triangle))
        TriangleMenu.addAction(classificationAction)

        # to get hypotenuse information
        hypotenuseAction = QAction('&Hypotenuse', self.__ui)
        hypotenuseAction.setShortcut('')
        hypotenuseAction.triggered.connect(lambda: self.entitiesActions('hypotenuse', 'Hypotenuse', Triangle))
        TriangleMenu.addAction(hypotenuseAction)
    
    def circleMenu(self):
        circleMenu = self.__menubar.addMenu('&Circle')

        # to create a circle   
        createCircle = QAction('&Create Circle', self.__ui)
        createCircle.setShortcut('Alt+3')
        createCircle.triggered.connect(lambda: self.drawEntity('circle'))
        circleMenu.addAction(createCircle)

        # calculate area and perimeter
        areaAndPerimeter = QAction('&Area and Perimeter', self.__ui)
        areaAndPerimeter.setShortcut('')
        areaAndPerimeter.triggered.connect(lambda: self.entitiesActions('areaPerimeter', "Area and Perimeter", Circle))
        circleMenu.addAction(areaAndPerimeter)

        # calculate radius and Diameter
        areaAndPerimeter = QAction('&Radius and Diameter', self.__ui)
        areaAndPerimeter.setShortcut('')
        areaAndPerimeter.triggered.connect(lambda: self.entitiesActions('radiusDiameter', "Radius and Diameter", Circle))
        circleMenu.addAction(areaAndPerimeter)

    def pointMenu(self):
        pMenu = self.__menubar.addMenu('&Point')

        # to create a Point   
        createPoint = QAction('&Create Point', self.__ui)
        createPoint.setShortcut('Alt+4')
        createPoint.triggered.connect(lambda: self.drawEntity('point'))
        pMenu.addAction(createPoint)

        # distance from origin
        distanceBetween = QAction('&Distance from Origin', self.__ui)
        distanceBetween.setShortcut('')
        distanceBetween.triggered.connect(lambda: self.entitiesActions('distanceOrigin', "Distance from Origin", Point))
        pMenu.addAction(distanceBetween)

        # distance: relation between 2 points
        distanceBetween = QAction('&Distance Between Two Points', self.__ui)
        distanceBetween.setShortcut('')
        distanceBetween.triggered.connect(lambda: self.entitiesActions('distanceBetween', "Distance Between Two Points", Point))
        pMenu.addAction(distanceBetween)

        # median: relation between 2 points
        medianBetween = QAction('&Median Between Two Points', self.__ui)
        medianBetween.setShortcut('')
        medianBetween.triggered.connect(lambda: self.entitiesActions('medianBetween', "Median Between Two Points", Point))
        pMenu.addAction(medianBetween)

        # check point proximity to a line   
        checkLineProximity = QAction('&Check Point Proximity to Line', self.__ui)
        checkLineProximity.setShortcut('')
        checkLineProximity.triggered.connect(lambda: self.entitiesRelationship('lineProximity', "Check Point Proximity to Line", Point, Line))
        pMenu.addAction(checkLineProximity)
  
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
        # get line equation
        lineEquation = QAction('&Line Equation', self.__ui)
        lineEquation.setShortcut('')
        lineEquation.triggered.connect(lambda: self.entitiesActions('equation', "Get Equation", Line))
        lineMenu.addAction(lineEquation)

        # to check if 2 lines are parallels 
        parallelLines = QAction('&Check parallelism', self.__ui)
        parallelLines.setShortcut('')
        parallelLines.triggered.connect(lambda: self.entitiesActions('areParallel', "Check parallelism", Line))
        lineMenu.addAction(parallelLines)

        # to get intersection point
        parallelLines = QAction('&Intersection Point', self.__ui)
        parallelLines.setShortcut('')
        parallelLines.triggered.connect(lambda: self.entitiesActions('intersection', "Intersection Point", LineSegment))
        lineMenu.addAction(parallelLines)

    def EntitiesMenu(self):
        entitiesMenu = self.__menubar.addMenu('&All Entities')

        # to manage all entities
        manageEntities = QAction('&Manage Entities', self.__ui)
        manageEntities.setShortcut('Alt+0')
        manageEntities.triggered.connect(lambda: AllFiguresInformation(self.__ui, "Manage Entities").open())
        entitiesMenu.addAction(manageEntities)

        # to delete all entities   
        deleteEntities = QAction('&Delete All Entities', self.__ui)
        deleteEntities.setShortcut('')
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
        elif type == 'Triangle':
            dialog = TriangleDialog(self.__ui)
            if dialog.exec_() == QDialog.Accepted:
                triang_data = dialog.getData()
                self.__ui.getCartesianPlane().addEntity(Triangle(triang_data[0], 
                                                                Point('Point 1',triang_data[1][0], triang_data[1][1]), 
                                                                Point('Point 2', triang_data[2][0], triang_data[2][1]), 
                                                                Point('Point 3', triang_data[3][0], triang_data[3][1]), 
                                                                triang_data[4]))
        elif type == 'circle':
            dialog = CircleDialog(self.__ui)
            if dialog.exec_() == QDialog.Accepted:
                circle_data = dialog.getData()
                self.__ui.getCartesianPlane().addEntity(Circle(f'{circle_data[0]}',
                                                        Point('central_p', circle_data[1][0], circle_data[1][1]), 
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

    def entitiesActions(self, action, actionName, classEntity):
        actionStatus = False
        if classEntity == Point:
            if action == "distanceOrigin":
                dialog = EntityActionDialog(self.__ui, actionName, classEntity, False)
                if dialog.exec_() == QDialog.Accepted:
                    data = dialog.getData()
                    p1 = self.__ui.getCartesianPlane().getAEntitieByName(data[0])
                    result = f'<b>{p1.distanceFromOrigin():.2f}</b>'
                    actionStatus = True
            else:
                dialog = EntityActionDialog(self.__ui, actionName, classEntity, True)
                if dialog.exec_() == QDialog.Accepted:
                    data = dialog.getData()
                    if action == "distanceBetween" or action == "medianBetween":
                        p1 = self.__ui.getCartesianPlane().getAEntitieByName(data[0])
                        p2 = self.__ui.getCartesianPlane().getAEntitieByName(data[1])
                        result = f'<b>{Point.distanceTo(p1, p2):.2f}</b>' if action == "distanceBetween" else f'<b>{p1.medianBetween(p2)}</b>'
                        actionStatus = True
        elif classEntity == Line or classEntity == LineSegment:
            if action == 'equation':
                dialog = EntityActionDialog(self.__ui, actionName, classEntity, False)
                if dialog.exec_() == QDialog.Accepted:
                    data = dialog.getData()
                    l1 = self.__ui.getCartesianPlane().getAEntitieByName(data[0])
                    result = f'<br><b>{l1.equation()}</b>'
                    actionStatus = True
            else:
                dialog = EntityActionDialog(self.__ui, actionName, classEntity, True)
                if dialog.exec_() == QDialog.Accepted:
                    data = dialog.getData()
                    l1 = self.__ui.getCartesianPlane().getAEntitieByName(data[0])
                    l2 = self.__ui.getCartesianPlane().getAEntitieByName(data[1])
                    if action == "areParallel":
                        result = "<b>Are parallel</b>" if l1.areParallels(l2) else "<b>Are not parallel</b>"
                        actionStatus = True
                    elif action == "intersection":
                        result = f" <b>{l1.intersection(l2)}</b>"
                        actionStatus = True
        else:
            dialog = ShapesActionsDialog(self.__ui, actionName, classEntity)
            
            if dialog.exec_() == QDialog.Accepted:
                data = dialog.getData()
                entity = self.__ui.getCartesianPlane().getAEntitieByName(data[0])
                
                if action == "areaPerimeter":
                    calcResult = [entity.area(), entity.perimeter()]
                    result = f"<br>Area: <b>{calcResult[0]:.2f}</b><br>Perimeter: <b>{calcResult[1]:.2f}</b>"
                elif classEntity == Rectangle and action == "widthHeight":
                    calcResult = [entity.width(), entity.height()]
                    result = f"<br>Width: <b>{calcResult[0]:.2f}</b><br>Height: <b>{calcResult[1]:.2f}</b>"
                elif classEntity == Circle and action =="radiusDiameter":
                    calcResult = [entity.getRadius(), entity.diameter()]
                    result = f"<br>Radius: <b>{calcResult[0]:.2f}</b><br>Diameter: <b>{calcResult[1]:.2f}</b>"
                elif classEntity == Triangle: 
                    if action =="anglesSides":
                        calcResult = [
                                [round(num, 2) for num in entity.angles()],
                                [round(num, 2) for num in entity.sides()]]
                        result = f"<br>Angles: <b>{calcResult[0]}</b><br>Sides: <b>{calcResult[1]}</b>"
                    elif action =="hypotenuse":
                        calcResult = entity.hypotenuse()
                        result = f"<br>Hipotenuse: <b>{calcResult:.2f}</b>"
                    elif action =="classify":
                        calcResult = entity.classify()
                        result = f"<br>Triangle Classification: <b>{calcResult}</b>"
                actionStatus = True
        if actionStatus:
            OperationResult(self.__ui, 
                            f'The result of {actionName} operation is:{result}<br><br>For decimal numeric values, the result is only approximate.'
                            ).open()

    def entitiesRelationship(self, action, actionName, entity1, entity2):
        dialog = EntitiesRelationship(self.__ui, actionName, entity1, entity2)
        if dialog.exec_() == QDialog.Accepted:
            data = dialog.getData()

            point = self.__ui.getCartesianPlane().getAEntitieByName(data[0])
            line = self.__ui.getCartesianPlane().getAEntitieByName(data[1])
            result = None

            if action == "lineProximity":
                result = Point.lineSegmentProximity(point, line)

            OperationResult(self.__ui, 
                            f'The result of "{actionName}" operation is: <b>{result}</b>'
                            ).open()   
        
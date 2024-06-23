from abc import abstractmethod
from PyQt5.QtWidgets import QDesktopWidget, QDialog, QVBoxLayout, QLineEdit, QDialogButtonBox, QSpinBox, QTextEdit, QListWidget, QStackedLayout, QComboBox, QFormLayout, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from package.UI.Components import *
from package.maths.Shapes import *
from package.exceptions.Exceptions import InvalidShape
from package.maths.Point import Point
from package.maths.Line import Line

class Dialog(QDialog):
    def __init__(self, window, title, icon_path, geometry = [300,300,300,200]):
        super().__init__()
        self.window = window

        self.setWindowTitle(title)
        self.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
        self.setWindowIcon(QIcon(icon_path))
        self.centralize()

    def centralize(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def AreInputsFilled(self, widgets):
        all_filled = True

        for widget in widgets:
            if isinstance(widget, QLineEdit):
                value = widget.text()
                if not value:
                    all_filled = False
            elif isinstance(widget, QSpinBox):
                value = widget.value()
                if value == widget.minimum(): # minimum value == 0 (default)
                    all_filled = False
            elif isinstance(widget, QTextEdit):
                value = widget.toPlainText()
                if not value:
                    all_filled = False
            elif isinstance(widget, ColorPicker):
                pass

        if all_filled:
            return True
        else:
            return False
    
    @abstractmethod
    def AreInputsValid(self):
        pass

    @abstractmethod
    def getData(self):
        pass
    
    def defineMainLayout(self, n_points):
        # shape name input
        input_name = TextInput('Shape name: ', self)
        self.input_widgets.append(input_name.inputObject())

        for i in range (0, n_points):
            point = PointInput(f'Point {i+1}', self, self.form_layout)
            self.input_widgets.append(point.inputsObjects())

        # color picker input
        color_picker = ColorPicker()
        self.input_widgets.append(color_picker)
        color_picker.addColorPicker(self.layout, 'Shape color: ')

class RectangleDialog(Dialog):
    def __init__(self, window):
        super().__init__(window, "Insert Rectangle information", './images/rect_icon.png')
        self.input_widgets = []

        # creating the main layout
        self.layout = QVBoxLayout()
        self.form_layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.defineMainLayout(4)
        self.setLayout(self.layout)

        # creating a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(lambda: self.accept() if self.AreInputsValid() else None)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def getData(self):
        return [
        self.input_widgets[0].text(),
        (self.input_widgets[1][0].value(), self.input_widgets[1][1].value()),
        (self.input_widgets[2][0].value(), self.input_widgets[2][1].value()),
        (self.input_widgets[3][0].value(), self.input_widgets[3][1].value()),
        (self.input_widgets[4][0].value(), self.input_widgets[4][1].value()),
        self.input_widgets[5].getCurrentColor()
        ]

    def AreInputsValid(self):
        if not self.AreInputsFilled(self.input_widgets):
            MessageBox(self).showMessage('Incomplete information!', 'You must fill all fields.')
            return False

        points = self.getData()[1:5] 

        try:
            rect = Rectangle('rect', 
                    Point('Point 1', points[0][0], points[0][1]), 
                    Point('Point 2', points[1][0], points[1][1]), 
                    Point('Point 3', points[2][0], points[2][1]), 
                    Point('Point 4', points[3][0], points[3][1]), 
                    '#000')
            
            self.window.getCartesianPlane().canAddFigure(rect) # to verify if this shape already exists in the plane
        except InvalidShape as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
  
class TrianguleDialog(Dialog):
    def __init__(self, window):
        super().__init__(window, "Insert Triangule Information", './images/rect_icon.png')
        self.input_widgets = []

       # creating the main layout
        self.layout = QVBoxLayout()
        self.form_layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.defineMainLayout(3)
        self.setLayout(self.layout)

        # creating a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(lambda: self.accept() if self.AreInputsValid() else None)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def getData(self):
        return [
        self.input_widgets[0].text(),
        (self.input_widgets[1][0].value(), self.input_widgets[1][1].value()),
        (self.input_widgets[2][0].value(), self.input_widgets[2][1].value()),
        (self.input_widgets[3][0].value(), self.input_widgets[3][1].value()),
        self.input_widgets[4].getCurrentColor()
        ]
        
    def AreInputsValid(self):
        if not self.AreInputsFilled(self.input_widgets):
            MessageBox(self).showMessage('Incomplete information!', 'You must fill all fields.')
            return False
        
        points = self.getData()[1:4] 

        try:
            triang = Triangule('rect', 
                    Point('Point 1', points[0][0], points[0][1]), 
                    Point('Point 2', points[1][0], points[1][1]), 
                    Point('Point 3', points[2][0], points[2][1]), 
                    '#000')
            
            self.window.getCartesianPlane().canAddFigure(triang) # to verify if this shape already exists in the plane
        except InvalidShape as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

class CircleDialog(Dialog):
    def __init__(self, window):
        super().__init__(window, "Insert Circle Information", './images/rect_icon.png')
        self.input_widgets = []

       # creating the main layout
        self.layout = QVBoxLayout()
        self.form_layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.defineMainLayout()
        self.setLayout(self.layout)

        # creating a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(lambda: self.accept() if self.AreInputsValid() else None)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def getData(self):
        return [
        self.input_widgets[0].text(),
        (self.input_widgets[1][0].value(), self.input_widgets[1][1].value()),
        self.input_widgets[2].value(),
        self.input_widgets[3].getCurrentColor()
        ]
        
    def AreInputsValid(self):
        if not self.AreInputsFilled(self.input_widgets):
            MessageBox(self).showMessage('Incomplete information!', 'You must fill all fields.')
            return False
        
        data = self.getData()[1:3] 

        try:
            circle = Circle('test', 
                    Point('Point 1', data[0][0], data[0][1]),
                    data[1],
                    '#000')
            
            self.window.getCartesianPlane().canAddFigure(circle) # to verify if this shape already exists in the plane
        except InvalidShape as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
    
    def defineMainLayout(self):
        # shape name input
        input_name = TextInput('Shape name: ', self)
        self.input_widgets.append(input_name.inputObject())

        # central point input
        point = PointInput(f'Point: ', self, self.form_layout)
        self.input_widgets.append(point.inputsObjects())

        # radius input
        row = QHBoxLayout()
        row.addWidget(QLabel("Radius: "))
        radius_input = QSpinBox(self)
        row.addWidget(radius_input)

        self.input_widgets.append(radius_input)
        self.form_layout.addLayout(row)
        # color picker input
        color_picker = ColorPicker()
        self.input_widgets.append(color_picker)
        color_picker.addColorPicker(self.layout, 'Shape color: ')

class LineDialog(Dialog):
    def __init__(self, window):
        super().__init__(window, "Insert Line information", './images/rect_icon.png')
        self.input_widgets = []

        # creating the main layout
        self.layout = QVBoxLayout()
        self.form_layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.defineMainLayout()
        self.setLayout(self.layout)

        # creating a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(lambda: self.accept() if self.AreInputsValid() else None)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def getData(self):
        return [
        self.input_widgets[0].text(),
        (self.input_widgets[1][0].value(), self.input_widgets[1][1].value()),
        (self.input_widgets[2][0].value(), self.input_widgets[2][1].value()),
        self.input_widgets[3].getCurrentColor()
        ]
        
    def AreInputsValid(self):
        if not self.AreInputsFilled(self.input_widgets):
            MessageBox(self).showMessage('Incomplete information!', 'You must fill all fields.')
            return False
        
        data = self.getData()[1:3] 

        try:
            line = Line('test', 
                    Point('Point 1', data[0][0], data[0][1]),
                    Point('Point 2', data[1][0], data[1][1]),
                    '#FFF')
            
            self.window.getCartesianPlane().canAddFigure(line) # to verify if this shape already exists in the plane
        except InvalidShape as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True
    
    def defineMainLayout(self):
        # shape name input
        input_name = TextInput('Shape name: ', self)
        self.input_widgets.append(input_name.inputObject())

        # point1 input
        point1 = PointInput(f'Point 1: ', self, self.form_layout)
        self.input_widgets.append(point1.inputsObjects())

        # point2 input
        point2 = PointInput(f'Point 2: ', self, self.form_layout)
        self.input_widgets.append(point2.inputsObjects())

        # color picker input
        color_picker = ColorPicker()
        self.input_widgets.append(color_picker)
        color_picker.addColorPicker(self.layout, 'Points color: ')


class PointDialog(Dialog):
    def __init__(self, window):
        super().__init__(window, "Insert Point information", './images/rect_icon.png')
        self.input_widgets = []

        # creating the main layout
        self.layout = QVBoxLayout()
        self.form_layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.defineMainLayout()
        self.setLayout(self.layout)

        # creating a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(lambda: self.accept() if self.AreInputsValid() else None)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def getData(self):
        return [
            self.input_widgets[0].text(),
            (self.input_widgets[1][0].value(), self.input_widgets[1][1].value()),
            self.input_widgets[2].getCurrentColor()
        ]
        
    def AreInputsValid(self):
        if not self.AreInputsFilled(self.input_widgets):
            MessageBox(self).showMessage('Incomplete information!', 'You must fill all fields.')
            return False

        coords = self.getData()[1]

        try:
            point = Point('test', coords[0], coords[1])
            self.window.getCartesianPlane().canAddFigure(point) # to verify if this shape already exists in the plane
        except InvalidShape as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

    def defineMainLayout(self):
        # shape name input
        input_name = TextInput('Point name: ', self)
        self.input_widgets.append(input_name.inputObject())

        point = PointInput('Coords: ', self, self.form_layout)
        self.input_widgets.append(point.inputsObjects())

        # color picker input
        color_picker = ColorPicker()
        color_picker.setCurrentColor('#000')
        self.input_widgets.append(color_picker)
        color_picker.addColorPicker(self.layout, 'Point color: ')

class PointActionsDialog(Dialog):
    def __init__(self, action, window, windowName, windowIcon = './images/rect_icon.png'):
        super().__init__(window, windowName, windowIcon, [300,300,300,150])
        self.input_widgets = []
        self.layout_type = 'one' if action == 'distanceOrigin' else 'two'   # layout type 'one': has input for only 1 point. Layout type 'two' has input for 2 points
                                                                            # the action 'distanceOrigin' requires only 1 point input
        # creating the main layout
        self.layout = QVBoxLayout()
        self.defineMainLayout()
        self.setLayout(self.layout)

        # creating a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(lambda: self.accept() if self.AreInputsValid() else None)
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def getData(self):
        if self.layout_type == 'two':
            if self.input_widgets[0].currentIndex() == 0:
                return [
                    'names',
                    self.input_widgets[1].text(),
                    self.input_widgets[2].text() if self.layout_type == 'two' else None
                ]

            else:
                return [
                    'coords',
                    (self.input_widgets[3][0].value(), self.input_widgets[3][1].value()),
                    (self.input_widgets[4][0].value(), self.input_widgets[4][1].value()) if self.layout_type == 'two' else None
                ]
        else:

            if self.input_widgets[0].currentIndex() == 0:
                return [
                    'names',
                    self.input_widgets[1].text(),
                ]

            else:
                return [
                    'coords',
                    (self.input_widgets[2][0].value(), self.input_widgets[2][1].value()),
                ]
        
    def AreInputsValid(self):
        if self.layout_type == 'two':
            if self.input_widgets[0].currentIndex() == 0:
                if (not self.input_widgets[1].text()) or (not self.input_widgets[2].text()):
                    MessageBox(self).showMessage('Alert!', 'Inputs are not valid', 'Make sure that all fields are filled in')
                    return False
                return True
            
            else:  
                if ((self.input_widgets[3][0].value() == self.input_widgets[4][0].value()) and (self.input_widgets[3][1].value() == self.input_widgets[4][1].value())):
                    MessageBox(self).showMessage('Alert!', 'Inputs are not valid', 'The points can not be the same.')
                    return False
                return True
        else:
            if self.input_widgets[0].currentIndex() == 0:
                if (not self.input_widgets[1].text()):
                    MessageBox(self).showMessage('Alert!', 'Inputs are not valid', 'Make sure that all fields are filled in')
                    return False
            return True
    def defineMainLayout(self):
        comboBox = QComboBox(self)
        comboBox.addItem("Select points by their names")
        comboBox.addItem("Select points by their coords ")
        self.input_widgets.append(comboBox)
        
        # Conectar o sinal de mudança de seleção a um método
        comboBox.currentIndexChanged.connect(self.onSelectionChange)

        # Criação de layouts para os diferentes formulários
        nameFormLayout = QWidget()
        nameFormLayoutLayout = QFormLayout(nameFormLayout)
        positionFormLayout = QWidget()
        positionFormLayoutLayout = QFormLayout(positionFormLayout)

        # Criação de widgets para a opção "Escrever nome dos pontos"
        n_input = 2 if self.layout_type == 'two' else 1
        for i in range(0,n_input):
            namePoint = QLineEdit(self)
            nameFormLayoutLayout.addRow(QLabel(f"Point {i+1}:"), namePoint)
            self.input_widgets.append(namePoint)


        # Criação de widgets para a opção "Inserir posição de cada ponto"
        for i in range(0,n_input):
            desc_label = QLabel(f"Point {i+1}:")
            
            x_input = QSpinBox(self)
            x_input.setMinimumWidth(100)
            x_input.setMaximumWidth(100)

            y_input = QSpinBox(self)
            y_input.setMinimumWidth(100)
            y_input.setMaximumWidth(100)

            h_layout = QHBoxLayout()
            h_layout.addWidget(desc_label)
            h_layout.addWidget(QLabel("X:"))
            h_layout.addWidget(x_input)
            h_layout.addWidget(QLabel("Y:"))
            h_layout.addWidget(y_input)

            positionFormLayoutLayout.addRow(h_layout)
            self.input_widgets.append((x_input, y_input))

        # Criação do QStackedWidget para alternar entre os formulários
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(nameFormLayout)
        self.stackedWidget.addWidget(positionFormLayout)

        # Adicionar o QComboBox e o QStackedWidget ao layout
        self.layout.addWidget(comboBox)
        self.layout.addWidget(self.stackedWidget)

        self.setLayout(self.layout)

    def onSelectionChange(self, index):
        # Alternar o QStackedWidget para exibir o formulário apropriado
        self.stackedWidget.setCurrentIndex(index) 

class FiguresInformation(Dialog):
    def __init__(self, window, cartesianPlane):
        super().__init__(window, 'All Shapes', './images/rect_icon.png', [300,300,300,400])
        
        self.shapes = cartesianPlane.getFigures()
        self.item_info = {}

        for shape in self.shapes:
            self.item_info[shape.getName()] = shape.info()
        
        # creating the main layout
        self.layout = QVBoxLayout()
        self.stacked_layout = QStackedLayout()
        self.list_page = QWidget() # list of shapes page
        self.info_page = QWidget() # page of selected shape info
        self.setLayout(self.layout)
        self.defineMainLayout()

    def open(self):
        if self.exec_() == QDialog.Accepted:
            self.window.update()

    def defineMainLayout(self):
        # to creat the stacked layout
        self.stacked_layout = QStackedLayout()

        # list of shapes page
        list_layout = QVBoxLayout()
        list_widget = QListWidget()
        
        shapes_name = []
        for shape in self.shapes:
            shapes_name.append(shape.getName())

        list_widget.addItems(shapes_name)
        list_widget.itemClicked.connect(self.displayItemInfo)
        list_layout.addWidget(list_widget)
        self.list_page.setLayout(list_layout)
        
        self.emptyListChecker() # show the advise "insert a shape" if the list is empty 

        self.stacked_layout.addWidget(self.list_page)
        self.stacked_layout.addWidget(self.info_page)

        self.layout.addLayout(self.stacked_layout)

        self.stacked_layout.setCurrentWidget(self.list_page)

    def displayItemInfo(self, item):
         # selected shape info page
        info_layout = QVBoxLayout()
        
        back_button = QPushButton('Return')
        back_button.setFixedSize(50, 20)
        back_button.clicked.connect(self.showMainMenu)
        
        self.info_label = QLabel('Click on a item to see it information.')
        self.info_label.setAlignment(Qt.AlignCenter)

        item_text = item.text()

        shape_info = self.item_info.get(item_text, 'Informações não disponíveis.')
        self.info_label.setText(shape_info)
        button_row = QHBoxLayout()
        button1 = QPushButton('Delete')
        button1.clicked.connect(lambda: self.deleteShapeAction(item_text))
        button2 = QPushButton('Edit')
        button_row.addWidget(button1)
        button_row.addWidget(button2)

        info_layout.addWidget(back_button)
        info_layout.addWidget(self.info_label)
        self.info_page.setLayout(info_layout)
        info_layout.addLayout(button_row)

        
        self.stacked_layout.setCurrentWidget(self.info_page)

    def showMainMenu(self):
        # Mostrar a página da lista
        self.stacked_layout.setCurrentWidget(self.list_page)

    def emptyListChecker(self):
        if not self.item_info:
            self.empty_label = QLabel('Insert a shape to see it information here ;)')
            self.layout.addWidget(self.empty_label)
            self.empty_label.setAlignment(Qt.AlignCenter)
    
    def deleteShapeAction(self, item):
        self.window.getCartesianPlane().deleteFigure(item)
        self.window.update()
        self.accept()

class DeleteFigures(Dialog):
    def __init__(self, window, cartesianPlane):
        super().__init__(window, 'All Shapes', './images/rect_icon.png', [100,100,200,100])

        # creating the main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.defineMainLayout()

    def open(self):
        if self.exec_() == QDialog.Accepted:
            self.window.update()

    def defineMainLayout(self):
        labell = QLabel("<b>Are you sure?</b>")
        labell.setAlignment(Qt.AlignCenter) 
        label2 = QLabel("This action can not be reverted later. All information will be lost.")
        label2.setAlignment(Qt.AlignCenter) 
        
        row = QHBoxLayout() 

        yes_button = QPushButton('Yes')
        yes_button.clicked.connect(lambda: self.deleteFiguresAction())

        no_button = QPushButton('No')
        no_button.clicked.connect(lambda: self.accept())

        row.addWidget(yes_button)
        row.addWidget(no_button)
        
        self.layout.addWidget(labell)
        self.layout.addWidget(label2)
        self.layout.addLayout(row)

    def deleteFiguresAction(self):
        if not self.window.getCartesianPlane().getFigures():
            MessageBox(self).showMessage('Error!', 'You do not have any figures.', '')
            self.accept()
        else:
            self.window.getCartesianPlane().setFigures([])
            self.window.update()
            self.accept()


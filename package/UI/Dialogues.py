from abc import abstractmethod
from PyQt5.QtWidgets import QDesktopWidget, QDialog, QVBoxLayout, QLineEdit, QDialogButtonBox, QSpinBox, QMessageBox, QTextEdit, QListWidget, QStackedLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

from package.UI.Components import *
from package.maths.Shapes import *
from package.exceptions.Exceptions import InvalidShape
from package.maths.Point import Point

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
    
    def warning (self, text = "Invalid inputs!", info = "Please, insert valid inputs."):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Error")
        msg_box.setText(text)
        msg_box.setInformativeText(info)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.setDefaultButton(QMessageBox.Ok)

        # Show the message box and capture the user's response
        response = msg_box.exec_()
        
        if response == QMessageBox.Ok:
            msg_box.accept()

    @abstractmethod
    def getData(self):
        pass
    
    def defineMainLayout(self, n_points):
        # shape name input
        input_name = TextInput('Shape name: ', self)
        self.input_widgets.append(input_name.inputObject())

        for i in range (0, n_points):
            point = PointInput(f'Point {i+1}', self)
            self.input_widgets.append(point.inputsObjects())

        # color picker input
        color_picker = ColorPicker()
        self.input_widgets.append(color_picker)
        color_picker.addColorPicker(self.layout, 'Shape color: ')

    @abstractmethod
    def AreInputsValid(self):
        pass

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
            self.warning('Error!', e.message)
            return False
        
        return True
  
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
            return False

        coords = self.getData()[1]

        try:
            point = Point('test', coords[0], coords[1])
            self.window.getCartesianPlane().canAddFigure(point) # to verify if this shape already exists in the plane
        except InvalidShape as e:
            self.warning('Error!', e.message)
            return False
        
        return True

    def defineMainLayout(self):
        # shape name input
        input_name = TextInput('Point name: ', self)
        self.input_widgets.append(input_name.inputObject())

        point = PointInput('Coords: ', self)
        self.input_widgets.append(point.inputsObjects())

        # color picker input
        color_picker = ColorPicker()
        color_picker.setCurrentColor('#000')
        self.input_widgets.append(color_picker)
        color_picker.addColorPicker(self.layout, 'Point color: ')

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
            self.warning('Error!', e.message)
            return False
        
        return True

class ShapesInformation(Dialog):
    def __init__(self, window, cartesianPlane):
        super().__init__(window, 'All Shapes', './images/rect_icon.png', [300,300,300,400])
        
        self.shapes = cartesianPlane.getShapes()
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
        
        # selected shape info page
        info_layout = QVBoxLayout()
        
        back_button = QPushButton('Return')
        back_button.setFixedSize(50, 20)
        back_button.clicked.connect(self.showMainMenu)
        
        self.info_label = QLabel('Click on a item to see it information.')
        self.info_label.setAlignment(Qt.AlignCenter)

        button_row = QHBoxLayout()
        button1 = QPushButton('Delete Shape')
        button2 = QPushButton('Button 2')
        button_row.addWidget(button1)
        button_row.addWidget(button2)

        info_layout.addWidget(back_button)
        info_layout.addWidget(self.info_label)
        self.info_page.setLayout(info_layout)
        info_layout.addLayout(button_row)

        self.stacked_layout.addWidget(self.list_page)
        self.stacked_layout.addWidget(self.info_page)

        self.layout.addLayout(self.stacked_layout)

        self.stacked_layout.setCurrentWidget(self.list_page)

    def displayItemInfo(self, item):
        item_text = item.text()

        shape_info = self.item_info.get(item_text, 'Informações não disponíveis.')
        self.info_label.setText(shape_info)
        
        self.stacked_layout.setCurrentWidget(self.info_page)

    def showMainMenu(self):
        # Mostrar a página da lista
        self.stacked_layout.setCurrentWidget(self.list_page)

    def emptyListChecker(self):
        if not self.item_info:
            self.empty_label = QLabel('Insert a shape to see it information here ;)')
            self.layout.addWidget(self.empty_label)
            self.empty_label.setAlignment(Qt.AlignCenter)
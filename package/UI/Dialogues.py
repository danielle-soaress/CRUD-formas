from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QLabel, QDesktopWidget, QApplication, QMenu, QAction, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QFormLayout, QSpinBox, QHBoxLayout, QMessageBox, QTextEdit
from PyQt5.QtGui import QIcon
from package.UI.Components import *

class Dialog(QDialog):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def centralize(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def checkInputs(self, widgets):
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
    
class RectangleDialog(Dialog):
    def __init__(self, window):
        super().__init__(window)
        self.input_widgets = []

        # setting the main config: window title, width and height, icon and layout
        self.setWindowTitle("Insert Rectangle information")
        self.setGeometry(300, 300, 300, 200)
        self.setWindowIcon(QIcon('./images/rect_icon.png'))
        self.centralize()

        # creating the main layout
        self.layout = QVBoxLayout()
        self.form_layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.defineMainLayout()
        self.setLayout(self.layout)

        # creating a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(lambda: self.accept() if self.checkInputs(self.input_widgets) else self.warning())
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

    def defineMainLayout(self):
        # shape name input
        input_name = TextInput('Shape name: ', self)
        self.input_widgets.append(input_name.inputObject())

        for i in range (0,4):
            point = PointInput(f'Point {i+1}', self)
            self.input_widgets.append(point.inputsObjects())

        # color picker input
        color_picker = ColorPicker()
        self.input_widgets.append(color_picker)
        color_picker.addColorPicker(self.layout)

class PointDialog(Dialog):
    def __init__(self, window):
        super().__init__(window)
        self.input_widgets = []

        # setting the main config: window title, width and height, icon and layout
        self.setWindowTitle("Insert Rectangle information")
        self.setGeometry(300, 300, 300, 200)
        self.setWindowIcon(QIcon('./images/rect_icon.png'))
        self.centralize()

        # creating the main layout
        self.layout = QVBoxLayout()
        self.form_layout = QVBoxLayout()
        self.layout.addLayout(self.form_layout)
        self.defineMainLayout()
        self.setLayout(self.layout)

        # creating a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(lambda: self.accept() if self.checkInputs(self.input_widgets) else self.warning())
        self.button_box.rejected.connect(self.reject)
        self.layout.addWidget(self.button_box)

    def getData(self):
        return [
            self.input_widgets[0].text(),
            (self.input_widgets[1][0].value(), self.input_widgets[1][1].value()),
            self.input_widgets[2].getCurrentColor()
        ]

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
        color_picker.addColorPicker(self.layout)


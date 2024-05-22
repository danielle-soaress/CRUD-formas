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
            elif isinstance(widget, colorPicker):
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
    
    def openDialog(self):
        if dialog.exec_() == QDialog.Accepted:
            rect_data = dialog.getData()
            self.update()

    def defineMainLayout(self):
        # shape name input
        shape_desc = QLabel("Shape name:")
        shape_name = QLineEdit(self)
        self.input_widgets.append(shape_name)
        row = QHBoxLayout()
        row.addWidget(shape_desc)
        row.addWidget(shape_name)
        self.form_layout.addLayout(row)

        # point 1 input
        point1_desc = QLabel("Point 1")
        point1_x = QSpinBox(self)
        point1_y = QSpinBox(self)
        self.input_widgets.append((point1_x, point1_y))
        self.addLineToFormLayout(point1_desc, point1_x, point1_y)
        self.setSpinBoxSize(point1_x)
        self.setSpinBoxSize(point1_y)

        # point 2 input
        point2_desc = QLabel("Point 2")
        point2_x = QSpinBox(self)
        point2_y = QSpinBox(self)
        self.input_widgets.append((point2_x, point2_y))
        self.addLineToFormLayout(point2_desc, point2_x, point2_y)
        self.setSpinBoxSize(point2_x)
        self.setSpinBoxSize(point2_y)

        # point 3 input
        point3_desc = QLabel("Point 3")
        point3_x = QSpinBox(self)
        point3_y = QSpinBox(self)
        self.input_widgets.append((point3_x, point3_y))
        self.addLineToFormLayout(point3_desc, point3_x, point3_y)
        self.setSpinBoxSize(point3_x)
        self.setSpinBoxSize(point3_y)

        # point 4 input
        point4_desc = QLabel("Point 4")
        point4_x = QSpinBox(self)
        point4_y = QSpinBox(self)
        self.input_widgets.append((point4_x, point4_y))
        self.addLineToFormLayout(point4_desc, point4_x, point4_y)
        self.setSpinBoxSize(point4_x)
        self.setSpinBoxSize(point4_y)

        self.layout.addLayout(self.form_layout)

        # color picker input
        color_picker = colorPicker()
        self.input_widgets.append(color_picker)
        color_picker.addColorPicker(self.layout)

    def addLineToFormLayout(self, desc_label, x_input, y_input):
        row = QHBoxLayout()
        row.addWidget(desc_label)
        row.addWidget(QLabel("x:"))
        row.addWidget(x_input)
        row.addWidget(QLabel("y:"))
        row.addWidget(y_input)
        self.form_layout.addLayout(row)
    
    def setSpinBoxSize(self, spinbox):
        spinbox.setMinimumWidth(100)
        spinbox.setMaximumWidth(100)

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QColorDialog, QSpinBox, QMessageBox
from PyQt5.QtGui import QColor, QPixmap

class ColorPicker(QWidget):

    def __init__(self):
        self.__color = QColor('#0000FF')
    
    def setCurrentColor(self, color):
        self.__color = color

    def getCurrentColor(self):
        return self.__color

    def getInputColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.__color = color
            self.updateColorPreview()

    def addColorPicker(self, layout, label):
        color_layout = QHBoxLayout()

        color_label = QLabel(f'{label}')
        color_btn = QPushButton("Choose")
        color_btn.clicked.connect(lambda: self.getInputColor())

        color_layout.addWidget(color_label)
        color_layout.addWidget(color_btn)

        self.__color_preview = QLabel()  # Previsão da cor
        self.__color_preview.setFixedSize(20, 20)
        self.updateColorPreview()
        color_layout.addWidget(self.__color_preview)

        layout.addLayout(color_layout)

    def updateColorPreview(self):
        color_preview_pixmap = QPixmap(20, 20)
        color_preview_pixmap.fill(QColor(self.__color))
        self.__color_preview.setPixmap(color_preview_pixmap)

class PointInput(QWidget):

    def __init__(self, text_label, parent = None, layout = None):
        super().__init__(parent)
        self.parent = parent
        self.layout = layout

        self.point_desc = QLabel(text_label)
        self.x_input_point = QSpinBox(self.parent)
        self.y_input_point = QSpinBox(self.parent)
        self.addLineToFormLayout(self.point_desc, self.x_input_point, self.y_input_point)
        self.setSpinBoxSize(self.x_input_point)
        self.setSpinBoxSize(self.y_input_point)

    def addLineToFormLayout(self, desc_label, x_input, y_input):
        row = QHBoxLayout()
        row.addWidget(desc_label)
        row.addWidget(QLabel("x:"))
        row.addWidget(x_input)
        row.addWidget(QLabel("y:"))
        row.addWidget(y_input)
        self.layout.addLayout(row)
    
    @staticmethod
    def setSpinBoxSize(spinbox):
        spinbox.setMinimumWidth(100)
        spinbox.setMaximumWidth(100)

    def inputsObjects(self):
        return (self.x_input_point, self.y_input_point)
    
    def getInputsValue(self):
        return (self.x_input_point.value(), self.y_input_point.value())

class TextInput(QWidget):

    def __init__(self, text_label, parent = None):
        super().__init__(parent)
        self.parent = parent

        self.input_desc = QLabel(text_label)
        self.input_obj = QLineEdit(parent)
        self.input_obj.setMaxLength(10)
        row = QHBoxLayout()
        row.addWidget(self.input_desc)
        row.addWidget(self.input_obj)
        self.parent.form_layout.addLayout(row)

    def inputObject(self):
        return self.input_obj

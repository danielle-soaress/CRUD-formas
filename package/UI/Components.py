from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QDoubleSpinBox, QPushButton, QColorDialog, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QDialogButtonBox
from PyQt5.QtGui import QColor, QPixmap

class colorPicker(QWidget):

    def __init__(self):
        self.__color = QColor('#0000FF')
    
    def getCurrentColor(self):
        return self.__color

    def getInputColor(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.__color = color
            self.updateColorPreview()

    def addColorPicker(self, layout):
        color_layout = QHBoxLayout()

        color_label = QLabel(f"Shape color:")
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
        color_preview_pixmap.fill(self.__color)
        self.__color_preview.setPixmap(color_preview_pixmap)
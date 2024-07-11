from abc import abstractmethod
from PyQt5.QtWidgets import QDesktopWidget, QDialog, QLineEdit, QSpinBox, QTextEdit
from package.UI.components.Inputs import *

class Dialog(QDialog):
    def __init__(self, ui, title, geometry = [300,300,300,200]):
        super().__init__()
        self._ui = ui

        self.setWindowTitle(title)
        self.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
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
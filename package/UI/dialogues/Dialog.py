from abc import abstractmethod
<<<<<<< HEAD
from PyQt5.QtWidgets import QDesktopWidget, QDialog, QLineEdit, QSpinBox, QTextEdit, QVBoxLayout, QDialogButtonBox
from package.UI.components.Inputs import *
from package.exceptions.Exceptions import InvalidAction

=======
from PyQt5.QtWidgets import QDesktopWidget, QDialog, QLineEdit, QSpinBox, QTextEdit
from package.UI.components.Inputs import *
>>>>>>> 7c5d97ad7519b133910929f96041d8df5f8a9019

class Dialog(QDialog):
    def __init__(self, ui, title, geometry = [300,300,300,200]):
        super().__init__()
        self._ui = ui
<<<<<<< HEAD
        self._input_widgets = []

        # general settings
=======

>>>>>>> 7c5d97ad7519b133910929f96041d8df5f8a9019
        self.setWindowTitle(title)
        self.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
        self.centralize()

<<<<<<< HEAD
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

=======
>>>>>>> 7c5d97ad7519b133910929f96041d8df5f8a9019
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
<<<<<<< HEAD
        if not self.AreInputsFilled(self._input_widgets):
            raise InvalidAction('Incomplete information! You must fill all fields.')
        pass

    def getData(self):
        data = []
        for widget in self._input_widgets:
            if isinstance (widget, PointInput):
                data.append(widget.getInputsValue())
            elif isinstance(widget, QLineEdit):
                data.append(widget.text())
            elif isinstance(widget, QSpinBox):
                data.append(widget.value())
            elif isinstance(widget, QTextEdit):
                data.append(widget.toPlainText())
            elif isinstance(widget, ColorPicker):
                data.append(widget.getCurrentColor())
        return data

    def defineMainLayout(self, n_points):
        # shape name input
        input_name = TextInput('Shape name: ', self)
        self._input_widgets.append(input_name.inputObject())
        print(self._input_widgets)

        for i in range (0, n_points):
            point = PointInput(f'Point {i+1}', self, self.form_layout)
            self._input_widgets.append(point)

        # color picker input
        color_picker = ColorPicker()
        self._input_widgets.append(color_picker)
=======
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
>>>>>>> 7c5d97ad7519b133910929f96041d8df5f8a9019
        color_picker.addColorPicker(self.layout, 'Shape color: ')
from abc import abstractmethod
from PyQt5.QtWidgets import QDesktopWidget, QDialog, QLineEdit, QSpinBox, QTextEdit, QVBoxLayout, QDialogButtonBox, QFormLayout, QComboBox, QStackedWidget
from package.UI.components.Inputs import *
from package.exceptions.Exceptions import InvalidAction


class Dialog(QDialog):
    def __init__(self, ui, title, geometry = [300,300,300,200]):
        super().__init__()
        self._ui = ui
        self._input_widgets = []

        # general settings
        self.setWindowTitle(title)
        self.setGeometry(geometry[0], geometry[1], geometry[2], geometry[3])
        self.centralize()

        # creating the main layout
        self.layout = QVBoxLayout()
        
        # creating a button box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(lambda: self.accept() if self.AreInputsValid() else None)
        self.button_box.rejected.connect(self.reject)

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
                data.append(widget.getCurrentColor().name())
            elif isinstance(widget, QComboBox):
                data.append(widget.currentText())
        return data

    @abstractmethod
    def defineMainLayout(self):
        pass
    
    def createEntityForm(self, n_points, circle = False):
        self.form_layout = QVBoxLayout()
        # shape name input
        input_name = TextInput('Shape name: ', self)
        self._input_widgets.append(input_name.inputObject())
        
        if circle:
            # radius input
            row = QHBoxLayout()
            row.addWidget(QLabel("Radius: "))
            radius_input = QSpinBox(self)
            radius_input.setMaximum(10)
            row.addWidget(radius_input)
            self.form_layout.addLayout(row)
            
            #central point
            point = PointInput(f'Central Point: ', self, self.form_layout)
            self._input_widgets.append(point)
            self._input_widgets.append(radius_input)
        else:
            for i in range (0, n_points):
                point = PointInput(f'Point: ', self, self.form_layout)
                self._input_widgets.append(point)
        self.layout.addLayout(self.form_layout)
        
        # color picker input
        color_picker = ColorPicker()
        self._input_widgets.append(color_picker)
        color_picker.addColorPicker(self.layout, 'Shape color: ')
    
    def dupleForm(self, options, form1, form2):
        comboBox = QComboBox(self)
        comboBox.addItems(options)
        self._input_widgets.append(comboBox)
        
        # Conectar o sinal de mudança de seleção a um método
        comboBox.currentIndexChanged.connect(self.onSelectionChange)


        # Criação do QStackedWidget para alternar entre os formulários
        self.stackedWidget = QStackedWidget()
        self.stackedWidget.addWidget(form1)
        self.stackedWidget.addWidget(form2)

        # Adicionar o QComboBox e o QStackedWidget ao layout
        self.layout.addWidget(comboBox)
        self.layout.addWidget(self.stackedWidget)

        self.setLayout(self.layout)

    def comboBoxForm(self, options, quantity, labelInfo = False, labelText = None):
        self.form_layout = QVBoxLayout()
        for i in range (0,quantity):
            if labelInfo:
                label = QLabel(labelText)
            else:
                label = QLabel(f"Point {i+1}: ")
            comboBox = QComboBox(self)
            comboBox.addItems(options)

            self.form_layout.addWidget(label)
            self.form_layout.addWidget(comboBox)
            self._input_widgets.append(comboBox)
        
        self.layout.addLayout(self.form_layout)

    def comboBoxForm2(self, option1, option2, labelsText):
        self.form_layout = QVBoxLayout()
            
        label1 = QLabel(labelsText[0])
        comboBox1 = QComboBox(self)
        comboBox1.addItems(option1)
        self.form_layout.addWidget(label1)
        self.form_layout.addWidget(comboBox1)
        self._input_widgets.append(comboBox1)

        label2 = QLabel(labelsText[1])
        comboBox2 = QComboBox(self)
        comboBox2.addItems(option2)
        self.form_layout.addWidget(label2)
        self.form_layout.addWidget(comboBox2)
        self._input_widgets.append(comboBox2)

        self.layout.addLayout(self.form_layout)


    def onSelectionChange(self, index):
        # Alternar o QStackedWidget para exibir o formulário apropriado
        self.stackedWidget.setCurrentIndex(index) 
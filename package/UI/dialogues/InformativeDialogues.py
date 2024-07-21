import resources_rc

from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QDialog, QVBoxLayout, QListWidget, QStackedLayout, QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QIcon
from package.UI.dialogues.Dialog import Dialog
from package.UI.components.Inputs import TextInput, ColorPicker
from package.UI.components.MessageBox import MessageBox
from package.exceptions.Exceptions import *

class FigureInfoDialog(QDialog):
    def __init__(self, figure, ui=None):
        super().__init__(ui)
        self.setWindowTitle("Entity Info")
        self.setWindowIcon(QIcon(':/images/lupa.png'))
        self.__ui = ui
        self.__figure = figure
        self.__cartesianPlane = ui.getCartesianPlane()

        layout = QVBoxLayout(self)
        
        info_str = "\n".join([f"<b>{key}</b>: {value}<br><br>" for key, value in figure.info().items()])
        self.infoLabel = QLabel(info_str, self)
        layout.addWidget(self.infoLabel)

        button_layout = QHBoxLayout()

        edit_button = QPushButton("Edit", self)
        edit_button.clicked.connect(self.editFigure)
        button_layout.addWidget(edit_button)

        delete_button = QPushButton("Delete Entity", self)
        delete_button.clicked.connect(self.deleteFigure)
        button_layout.addWidget(delete_button)

        layout.addLayout(button_layout)

        return_button = QPushButton("Save", self)
        return_button.clicked.connect(self.accept)
        layout.addWidget(return_button)

    def editFigure(self):
        dialog = EditFigureDialog(self.__ui, [self.__figure.getName(), self.__figure.getFillColor()])
        if dialog.exec_() == QDialog.Accepted:
            data = dialog.getData()
            self.__figure.setName(data[0])
            self.__figure.setFillColor(data[1])

    def deleteFigure(self):
        self.__cartesianPlane.deleteEntity(self.__figure.getName())
        self.reject()

class EditFigureDialog(Dialog):
    def __init__(self, ui, data, title = "Edit Entity", geometry = [300,300,200,150]):
        super().__init__(ui, title,QIcon(':/images/editar.png'),  geometry)
        self.__data = data
        self.defineMainLayout()
        self.setLayout(self.layout)
        self.layout.addWidget(self.button_box)
    
    def AreInputsValid(self):
        try:
            super().AreInputsValid()

            data = self.getData()

            figuresName= self._ui.getCartesianPlane().getEntities()
            figuresName = list(map(lambda x: x.getName(), figuresName))

            if data[0] in figuresName and data[0] != self.__data[0]:
                raise InvalidName('An entity with that name already exists.')
        except InvalidAction as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        except InvalidName as e:
            MessageBox(self).showMessage('Error!', e.message)
            return False
        
        return True

    def defineMainLayout(self):
        MessageBox(self).showMessage("Alert!", "You can only edit the name and fill color.", "After editing a figure, you will see the result when you click the save button.")
        
        self.form_layout = QVBoxLayout()
        
        # shape name input
        input_name = TextInput('Shape name: ', self, self.__data[0])
        self._input_widgets.append(input_name.inputObject())

        self.layout.addLayout(self.form_layout)
        
        # color picker input
        color_picker = ColorPicker()
        color_picker.setCurrentColor(QColor(self.__data[1]))
        self._input_widgets.append(color_picker)
        color_picker.addColorPicker(self.layout, 'Shape color: ')

class AllFiguresInformation(QDialog):
    def __init__(self, ui, title, geometry=[300, 300, 300, 400]):
        super().__init__()
        self.setWindowIcon(QIcon(':/images/lista.png'))
        self._ui = ui
        self.setWindowTitle(title)
        self.setGeometry(*geometry)

        self.__entities = ui.getCartesianPlane().getEntities()
        self.item_info = {}

        for entity in self.__entities:
            self.item_info[entity.getName()] = entity.model()
        
        # creating the main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.stacked_layout = QStackedLayout()
        self.list_page = QWidget()  # list of shapes page
        self.info_page = QWidget()  # page of selected shape info
        self.defineMainLayout()

    def open(self):
        if self.exec_() == QDialog.Accepted:
            self._ui.update()

    def defineMainLayout(self):
        # list of shapes page
        list_layout = QVBoxLayout()
        list_widget = QListWidget()

        shapes_name = [shape.getName() for shape in self.__entities]
        list_widget.addItems(shapes_name)
        list_widget.itemClicked.connect(self.displayItemInfo)
        list_layout.addWidget(list_widget)
        
        if not self.list_page.layout():  # Only set layout if it doesn't already have one
            self.list_page.setLayout(list_layout)

        self.emptyListChecker()  # show the advice "insert a shape" if the list is empty 

        self.stacked_layout.addWidget(self.list_page)
        self.stacked_layout.addWidget(self.info_page)

        self.layout.addLayout(self.stacked_layout)

        self.stacked_layout.setCurrentWidget(self.list_page)

    def displayItemInfo(self, item):
        # selected shape info page
        if self.info_page.layout():  # Remove existing layout if there is one
            old_layout = self.info_page.layout()
            QWidget().setLayout(old_layout)
        
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
        button2.clicked.connect(lambda: self.editFigure(item_text))
        button_row.addWidget(button1)
        button_row.addWidget(button2)

        info_layout.addWidget(back_button)
        info_layout.addWidget(self.info_label)
        info_layout.addLayout(button_row)
        
        self.info_page.setLayout(info_layout)
        self.stacked_layout.setCurrentWidget(self.info_page)

    def editFigure(self, item):
        dialog = EditFigureDialog(self._ui)
        if dialog.exec_() == QDialog.Accepted:
            entity = self._ui.getCartesianPlane().getAEntitieByName(item)
            data = dialog.getData()
            entity.setName(data[0])
            entity.setFillColor(data[1])
        
        self.reject

    def showMainMenu(self):
        # Mostrar a página da lista
        self.stacked_layout.setCurrentWidget(self.list_page)

    def emptyListChecker(self):
        if not self.item_info:
            self.empty_label = QLabel('Insert a shape to see it information here ;)')
            self.empty_label.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(self.empty_label)
    
    def deleteShapeAction(self, item):
        self._ui.getCartesianPlane().deleteEntity(item)
        self._ui.update()
        self.accept()
        
class DeleteEntities(Dialog):
    def __init__(self,  ui, title, geometry = [100,100,200,100]):
        super().__init__(ui,title, QIcon(':/images/apagar.png'), geometry)
        # creating the main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.defineMainLayout()
        
    def open(self):
        if self.exec_() == QDialog.Accepted:
            self._ui.update()

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
        if not self._ui.getCartesianPlane().getEntities():
            MessageBox(self).showMessage('Error!', 'You do not have any figures.', '')
            self.accept()
        else:
            self._ui.getCartesianPlane().reset()
            self._ui.update()
            self.accept()

class OperationResult(Dialog):
    def __init__(self,  ui, operationResultText, title = 'Operation Result', geometry = [300,300,100,100]):
        super().__init__(ui,title, QIcon(':/images/calculadora.png'), geometry)
        self.__op_result_text = operationResultText
        self.centralize()
        # creating the main layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.defineMainLayout()
        
    def open(self):
        if self.exec_() == QDialog.Accepted:
            self._ui.update()

    def defineMainLayout(self):
        label1 = QLabel(self.__op_result_text)
        row = QHBoxLayout()
        row.addWidget(label1)
        self.layout.addLayout(row)

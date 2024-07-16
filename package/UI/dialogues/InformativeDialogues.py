from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton, QHBoxLayout, QDialog, QVBoxLayout, QListWidget, QStackedLayout, QWidget
from PyQt5.QtCore import Qt
from package.UI.dialogues.Dialog import Dialog
from package.UI.components.MessageBox import MessageBox

class FigureInfoDialog(QDialog):
    def __init__(self, figure, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Figure Info")
        self.__figure = figure
        self.__cartesianPlane = parent.getCartesianPlane()

        layout = QVBoxLayout(self)

        # Adicione os campos de informações da figura aqui
        self.infoLabel = QLabel(figure.model(), self)
        layout.addWidget(self.infoLabel)

        # Layout para os botões "Edit" e "Delete Figure"
        button_layout = QHBoxLayout()

        edit_button = QPushButton("Edit", self)
        edit_button.clicked.connect(self.editFigure)
        button_layout.addWidget(edit_button)

        delete_button = QPushButton("Delete Figure", self)
        delete_button.clicked.connect(self.deleteFigure)
        button_layout.addWidget(delete_button)

        layout.addLayout(button_layout)

        # Botão "Save"
        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.saveInfo)
        layout.addWidget(save_button)

    def saveInfo(self):
        # Salvar as informações editadas da figura
        self.__figure.setName(self.nameField.text())
        self.accept()

    def editFigure(self):
        # Implemente a lógica para editar a figura (se necessário)
        pass

    def deleteFigure(self):
        self.__cartesianPlane.deleteEntity(self.__figure.getName())
        self.reject()

class AllFiguresInformation(Dialog):
    def __init__(self,  ui, title):
        super().__init__(ui,title)
        self.setGeometry(300,300,300,400)
        self.centralize()
        
        self.shapes = ui.getCartesianPlane().getEntities()
        self.item_info = {}

        for shape in self.shapes:
            self.item_info[shape.getName()] = shape.model()
        
        # creating the main layout
        self.layout = QVBoxLayout()
        self.stacked_layout = QStackedLayout()
        self.list_page = QWidget() # list of shapes page
        self.info_page = QWidget() # page of selected shape info
        self.setLayout(self.layout)
        self.defineMainLayout()

    def open(self):
        if self.exec_() == QDialog.Accepted:
            self._ui.update()

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
        self._ui.getCartesianPlane().deleteEntity(item)
        self._ui.update()
        self.accept()

class DeleteEntities(Dialog):
    def __init__(self,  ui, title):
        super().__init__(ui,title)
        self.setGeometry(100,100,200,100)
        self.centralize()
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
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout

class FigureInfoDialog(QDialog):
    def __init__(self, figure, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Figure Info")
        self.figure = figure

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
        self.figure.setName(self.nameField.text())
        self.accept()

    def editFigure(self):
        # Implemente a lógica para editar a figura (se necessário)
        pass

    def deleteFigure(self):
        # Implemente a lógica para deletar a figura
        # Por exemplo, você pode emitir um sinal ou chamar um método no widget pai
        # Aqui, só fechamos a janela como exemplo
        self.reject()
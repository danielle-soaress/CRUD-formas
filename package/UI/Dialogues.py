from PyQt5.QtWidgets import QLabel, QDesktopWidget, QApplication, QMenu, QAction, QPushButton, QDialog, QVBoxLayout, QLabel, QLineEdit, QDialogButtonBox, QFormLayout
from PyQt5.QtGui import QIcon
class RectangleDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Rectangle information")
        self.setGeometry(300, 300, 300, 200)
        self.setWindowIcon(QIcon('./images/rect_icon.png'))

        self.layout = QVBoxLayout()

        self.form_layout = QFormLayout()
        self.x_input = QLineEdit()
        self.y_input = QLineEdit()
        self.width_input = QLineEdit()
        self.height_input = QLineEdit()

        self.form_layout.addRow("X:", self.x_input)
        self.form_layout.addRow("Y:", self.y_input)
        self.form_layout.addRow("Width:", self.width_input)
        self.form_layout.addRow("Height:", self.height_input)

        self.layout.addLayout(self.form_layout)

        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.button_box.accepted.connect(self.accept)
        self.button_box.rejected.connect(self.reject)

        self.layout.addWidget(self.button_box)
        self.setLayout(self.layout)
        self.centralize()

    def centralize(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    def get_data(self):
        return (int(self.x_input.text()), int(self.y_input.text()), int(self.width_input.text()), int(self.height_input.text()))
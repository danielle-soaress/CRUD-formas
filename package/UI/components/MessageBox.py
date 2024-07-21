import resources_rc

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox

class MessageBox():
    def __init__(self, parent = None, ):
        self.parent = parent

    def showMessage(self, title="Alert", message="Something is wrong...", detailed_text="Review your inputs and try again.", icon = QMessageBox.Warning):
        msg = QMessageBox(self.parent)
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setWindowIcon(QIcon(':/images/aviso.png'))
        msg.setText(message)
        msg.setInformativeText(detailed_text)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        
        retval = msg.exec_()
        return retval
import sys
from PyQt5.QtWidgets import QApplication
from package.UI.MainUI import MainUI

def workspace():
	ui = MainUI()
	ui.run()

if __name__ == "__main__":
	workspace()

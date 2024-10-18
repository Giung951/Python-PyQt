"""
Refer to https://wikidocs.net/35489
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("label.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    windows popup window with 2 buttons & a label class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.changeText.clicked.connect(self.change_text_function)
        self.printText.clicked.connect(self.print_text_function)

    def change_text_function(self):
        """
        Change label when ChangeText is pressed
        """
        self.label.setText("This is Label - Change Text")

    def print_text_function(self):
        """
        Output message when PrintText is pressed
        """
        print(self.label.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

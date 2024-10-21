"""
Refer to https://wikidocs.net/35489
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("label.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    Windows popup window with 1 label and 2 buttons class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_changeText.clicked.connect(self.change_text_function)
        self.pushButton_printText.clicked.connect(self.print_text_function)

    def change_text_function(self):
        """
        Change label when 'Change Text' button is pressed
        """
        self.label_text.setText("This is Label - Change Text")

    def print_text_function(self):
        """
        Output message when 'Print Text' button is pressed
        """
        print(self.label_text.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

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

        self.pushButton_changeLabel.clicked.connect(self.change_label)
        self.pushButton_printLabel.clicked.connect(self.print_label)

    def change_label(self):
        """
        Change label when 'Change Label' button is pressed
        """
        self.label_text.setText("This is Label - Change Text")

    def print_label(self):
        """
        Output message when 'Print Label' button is pressed
        """
        print(self.label_text.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

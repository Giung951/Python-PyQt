"""
Refer to https://wikidocs.net/35485
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("push_button.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    Windows popup window with 2 buttons class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.button1.clicked.connect(self.button1_function)
        self.button2.clicked.connect(self.button2_function)

    def button1_function(self):
        """
        Output message when button1 is pressed
        """
        print("Button1 Clicked")

    def button2_function(self):
        """
        Output message when button2 is pressed
        """
        print("Button2 Clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

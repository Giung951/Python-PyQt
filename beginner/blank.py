"""
Refer to https://wikidocs.net/35482
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("untitled.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    Empty Windows popup window class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

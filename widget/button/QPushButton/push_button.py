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

        self.pushButton_button1.clicked.connect(self.push_button)
        self.pushButton_button2.clicked.connect(self.push_button)

    def push_button(self):
        """
        Output message when each button is pressed
        """
        push_button_is_pressed = self.sender()

        if push_button_is_pressed == self.pushButton_button1:
            print("Button1 Clicked")
        elif push_button_is_pressed == self.pushButton_button2:
            print("Button2 Clicked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

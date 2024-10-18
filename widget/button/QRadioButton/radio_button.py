"""
Refer to https://wikidocs.net/35486
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("radio_button.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    windows popup window with a group box containing 4 radio buttons class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.groupradio1.clicked.connect(self.groupbox_radio_function)
        self.groupradio2.clicked.connect(self.groupbox_radio_function)
        self.groupradio3.clicked.connect(self.groupbox_radio_function)
        self.groupradio4.clicked.connect(self.groupbox_radio_function)

    def groupbox_radio_function(self):
        """
        Output message when each radio button is pressed
        """
        if self.groupradio1.isChecked():
            print("GroupBox Radio1 Chekced")
        elif self.groupradio2.isChecked():
            print("GroupBox Radio2 Checked")
        elif self.groupradio3.isChecked():
            print("GroupBox Radio3 Checked")
        elif self.groupradio4.isChecked():
            print("GroupBox Radio4 Checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

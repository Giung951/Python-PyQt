"""
Refer to https://wikidocs.net/35486
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("radio_button.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    Windows popup window with 1 group box containing 4 radio buttons class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.groupBox_radioButton_radio1.clicked.connect(self.groupbox_radio_function)
        self.groupBox_radioButton_radio2.clicked.connect(self.groupbox_radio_function)
        self.groupBox_radioButton_radio3.clicked.connect(self.groupbox_radio_function)
        self.groupBox_radioButton_radio4.clicked.connect(self.groupbox_radio_function)

    def groupbox_radio_function(self):
        """
        Output message when each radio button is pressed
        """
        if self.groupBox_radioButton_radio1.isChecked():
            print("Group Box Radio1 Chekced")
        elif self.groupBox_radioButton_radio2.isChecked():
            print("Group Box Radio2 Checked")
        elif self.groupBox_radioButton_radio3.isChecked():
            print("Group Box Radio3 Checked")
        elif self.groupBox_radioButton_radio4.isChecked():
            print("Group Box Radio4 Checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

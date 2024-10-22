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

        self.groupBox_radioButton_radio1.clicked.connect(self.group_box_radio_button)
        self.groupBox_radioButton_radio2.clicked.connect(self.group_box_radio_button)
        self.groupBox_radioButton_radio3.clicked.connect(self.group_box_radio_button)
        self.groupBox_radioButton_radio4.clicked.connect(self.group_box_radio_button)

    def group_box_radio_button(self):
        """
        Output message when each radio button is checked
        """
        if self.groupBox_radioButton_radio1.isChecked():
            print("Radio1 Chekced")
        elif self.groupBox_radioButton_radio2.isChecked():
            print("Radio2 Checked")
        elif self.groupBox_radioButton_radio3.isChecked():
            print("Radio3 Checked")
        elif self.groupBox_radioButton_radio4.isChecked():
            print("Radio4 Checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

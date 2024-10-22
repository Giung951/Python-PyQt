"""
Refer to https://wikidocs.net/35488
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("check_box.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    Windows popup window with 4 check boxes and 1 group box containing 4 check boxes class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.checkBox_check1.stateChanged.connect(self.check_box)
        self.checkBox_check2.stateChanged.connect(self.check_box)
        self.checkBox_check3.stateChanged.connect(self.check_box)
        self.checkBox_check4.stateChanged.connect(self.check_box)

        self.groupBox_checkBox_check1.stateChanged.connect(self.group_box_check_box)
        self.groupBox_checkBox_check2.stateChanged.connect(self.group_box_check_box)
        self.groupBox_checkBox_check3.stateChanged.connect(self.group_box_check_box)
        self.groupBox_checkBox_check4.stateChanged.connect(self.group_box_check_box)

    def check_box(self):
        """
        Output message when each check box is checked
        """
        if self.checkBox_check1.isChecked():
            print("Check1 Checked")
        if self.checkBox_check2.isChecked():
            print("Check2 Checked")
        if self.checkBox_check3.isChecked():
            print("Check3 Checked")
        if self.checkBox_check4.isChecked():
            print("Check4 Checked")

    def group_box_check_box(self):
        """
        Output message when each check box is checked
        """
        if self.groupBox_checkBox_check1.isChecked():
            print("Check1 Checked")
        if self.groupBox_checkBox_check2.isChecked():
            print("Check2 Checked")
        if self.groupBox_checkBox_check3.isChecked():
            print("Check3 Checked")
        if self.groupBox_checkBox_check4.isChecked():
            print("Check4 Checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

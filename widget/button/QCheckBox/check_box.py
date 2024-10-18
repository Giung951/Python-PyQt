"""
Refer to https://wikidocs.net/35488
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("check_box.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    windows popup window with 4 check boxes & a group box containing 4 check boxes class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.check1.stateChanged.connect(self.check_function)
        self.check2.stateChanged.connect(self.check_function)
        self.check3.stateChanged.connect(self.check_function)
        self.check4.stateChanged.connect(self.check_function)

        self.groupcheck1.stateChanged.connect(self.groupbox_check_function)
        self.groupcheck2.stateChanged.connect(self.groupbox_check_function)
        self.groupcheck3.stateChanged.connect(self.groupbox_check_function)
        self.groupcheck4.stateChanged.connect(self.groupbox_check_function)

    def check_function(self):
        """
        Output message when each check box is checked
        """
        if self.check1.isChecked():
            print("Check1 Checked")
        if self.check2.isChecked():
            print("Check2 Checked")
        if self.check3.isChecked():
            print("Check3 Checked")
        if self.check4.isChecked():
            print("Check4 Checked")

    def groupbox_check_function(self):
        """
        Output message when each check box is checked
        """
        if self.groupcheck1.isChecked():
            print("GroupBox Check1 Checked")
        if self.groupcheck2.isChecked():
            print("GroupBox Check2 Checked")
        if self.groupcheck3.isChecked():
            print("GroupBox Check3 Checked")
        if self.groupcheck4.isChecked():
            print("GroupBox Check4 Checked")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

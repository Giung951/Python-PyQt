"""
Refer to https://wikidocs.net/35491
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("line_edit.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    Windows popup window with 1 label, 1 line edit and 1 push button class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit_line.textChanged.connect(self.line_edit_to_label)
        self.lineEdit_line.returnPressed.connect(self.print_line_edit)
        self.pushButton_changeText.clicked.connect(self.change_line_edit)

    def line_edit_to_label(self):
        """
        Input the text in line edit and output the input text in label
        """
        self.label_text.setText(self.lineEdit_line.text())

    def print_line_edit(self):
        """
        Output the input text in line edit when enter is pressed
        """
        print(self.lineEdit_line.text())

    def change_line_edit(self):
        """
        Change the text in line edit
        """
        self.lineEdit_line.setText("Change Text")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

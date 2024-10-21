"""
Refer to https://wikidocs.net/35491
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("line_edit.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    Windows popup window with 1 label, 2 line edit and push button class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.lineEdit_line.textChanged.connect(self.line_edit_text_function)
        self.lineEdit_line.returnPressed.connect(self.print_text_function)
        self.pushButton_changeText.clicked.connect(self.change_text_function)

    def line_edit_text_function(self):
        """
        Input text using line edit and output the input text
        """
        self.label_text.setText(self.lineEdit_line.text())

    def print_text_function(self):
        """
        When enter is pressed, output the input text using line edit
        """
        print(self.lineEdit_line.text())

    def change_text_function(self):
        """
        Change the text in line edit
        """
        self.lineEdit_line.setText("Change Text")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

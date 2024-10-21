"""
Refer to https://wikidocs.net/35490
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("text_browser.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    Windows popup window with 1 print button, 1 set text button, 1 append button and 1 clear button class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_printText.clicked.connect(self.print_text_function)
        self.pushButton_setText.clicked.connect(self.change_text_function)
        self.pushButton_appendText.clicked.connect(self.append_text_function)
        self.pushButton_clearText.clicked.connect(self.clear_text_function)

    def print_text_function(self):
        """
        Get the text written in text browser when 'Print Text' button is pressed
        """
        print(self.textbrow_Test.toPlainText())

    def change_text_function(self):
        """
        Set a new text in text browser when 'Set Text' button is pressed
        """
        self.textbrow_Test.setPlainText("This is Text Browser - Change Text")

    def append_text_function(self):
        """
        Add a text in text browser when 'Append Text' button is pressed
        """
        self.textbrow_Test.append("Append Text")

    def clear_text_function(self):
        """
        Clear the text written in text browser when 'Clear Text' button is pressed
        """
        self.textbrow_Test.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

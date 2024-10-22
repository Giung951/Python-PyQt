"""
Refer to https://wikidocs.net/35492
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic

form_class = uic.loadUiType("plain_text_edit.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    Windows popup window with 1 plain text edit and 3 push buttons class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pushButton_printPlainTextEdit.clicked.connect(self.print_plain_text_edit)
        self.pushButton_clearPlainTextEdit.clicked.connect(self.clear_plain_text_edit)
        self.pushButton_appendPlainTextEdit.clicked.connect(self.append_plain_text_edit)

    def print_plain_text_edit(self):
        """
        Output the input text in plain text edit when 'Print Text Edit' button is pressed
        """
        print(self.plainTextEdit_text.toPlainText())

    def clear_plain_text_edit(self):
        """
        Clear the input text in plain text edit when 'Clear Text Edit' button is pressed
        """
        self.plainTextEdit_text.clear()

    def append_plain_text_edit(self):
        """
        Add the specific text in plain text edit when 'Append Plain Text Edit' button is pressed
        """
        self.plainTextEdit_text.appendPlainText("Append Plain Text Edit")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

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

        self.pushButton_printTextBrowser.clicked.connect(self.print_text_browser)
        self.pushButton_setTextBrowser.clicked.connect(self.set_text_browser)
        self.pushButton_appendTextBrowser.clicked.connect(self.append_text_browser)
        self.pushButton_clearTextBrowser.clicked.connect(self.clear_text_browser)

    def print_text_browser(self):
        """
        Output the text in text browser when 'Print Text Browser' button is pressed
        """
        print(self.textBrowser_text.toPlainText())

    def set_text_browser(self):
        """
        Set a new text in text browser when 'Set Text Browser' button is pressed
        """
        self.textBrowser_text.setPlainText("This is Text Browser - Change Text")

    def append_text_browser(self):
        """
        Add the specific text in text browser when 'Append Text Browser' button is pressed
        """
        self.textBrowser_text.append("Append Text")

    def clear_text_browser(self):
        """
        Clear the text in text browser when 'Clear Text Browser' button is pressed
        """
        self.textBrowser_text.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

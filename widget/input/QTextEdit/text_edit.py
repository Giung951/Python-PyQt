"""
Refer to https://wikidocs.net/35492
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QColor, QFont
from PyQt5 import uic

form_class = uic.loadUiType("text_edit.ui")[0]


class WindowClass(QMainWindow, form_class):
    """
    Windows popup window with 1 text edit and 7 push buttons class
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.font_size = 10

        self.pushButton_printTextEdit.clicked.connect(self.print_text_edit)
        self.pushButton_clearTextEdit.clicked.connect(self.clear_text_edit)
        self.pushButton_setFont.clicked.connect(self.font_default)
        self.pushButton_setFontItalic.clicked.connect(self.font_italic)
        self.pushButton_setFontColor.clicked.connect(self.font_color_red)
        self.pushButton_fontSizeUp.clicked.connect(self.font_size_up)
        self.pushButton_fontSizeDown.clicked.connect(self.font_size_down)

    def print_text_edit(self):
        """
        Output the input text in text edit when 'Print Text Edit' button is pressed
        """
        print(self.textEdit_text.toPlainText())

    def clear_text_edit(self):
        """
        Clear the input text in text edit when 'Clear Text Edit' button is pressed
        """
        self.textEdit_text.clear()

    def font_default(self):
        """
        Set the input text to the specific font and font size
        """
        fonts = QFont("Apple SD Gothic Neo", 10)
        self.textEdit_text.setCurrentFont(fonts)

    def font_italic(self):
        """
        Set the font of the input text to italic
        """
        self.textEdit_text.setFontItalic(True)

    def font_color_red(self):
        """
        Set the color of the input text to red
        """
        colors = QColor(255, 0, 0)
        self.textEdit_text.setTextColor(colors)

    def font_size_up(self):
        """
        Size up the input text
        """
        self.font_size = self.font_size + 1
        self.textEdit_text.setFontPointSize(self.font_size)

    def font_size_down(self):
        """
        Size down the input text
        """
        self.font_size = self.font_size - 1
        self.textEdit_text.setFontPointSize(self.font_size)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

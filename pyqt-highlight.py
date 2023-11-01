

# not working

import sys
from PyQt5 import QtGui
from PyQt5 import QtCore


from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextCursor, QTextCharFormat, QSyntaxHighlighter
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QVBoxLayout, QWidget
import re
import keyword

class PythonHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super(PythonHighlighter, self).__init__(parent)

        self.comment_start = '#'
        color = QtGui.QColor()
        color.setNamedColor("red")
        self.comment_format = QTextCharFormat()
        print(Qt.red)
        self.comment_format.setForeground(color)
        self.highlighting_rules = []
        self.highlighting_rules += [
            (r'\b%s\b'% i , 0, self.comment_format) for i in keyword.kwlist
        ]

        self.rules = [(QtCore.QRegExp(pat), index, fmt) for (pat, index, fmt) in self.highlighting_rules]
        # print(self.rules)
    def highlightBlock(self, text):
        print("highlighting")
        print(self.highlighting_rules)
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)
         
            print(text)
            while index >= 0:
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

    def formatFor(self, name):
        if name == 'comment':
            return self.comment_format
        elif name == 'keyword':
            return self.keyword_format
        # Add more formatting rules as needed
        return QTextCharFormat()


class CodeEditor(QPlainTextEdit):
    def __init__(self):
        super().__init__()
        self.highlighter = PythonHighlighter(self.document())
        # self.show()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout()
        self.editor = CodeEditor()
        layout.addWidget(self.editor)

        self.central_widget.setLayout(layout)

        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('Python Code Editor')
        self.show()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "پای کیوت 5"
        self.top = 100
        self.left = 100
        self.width = 500
        self.height = 500
        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.show()

App = QApplication(sys.argv)
win = Window()
sys.exit(App.exec())
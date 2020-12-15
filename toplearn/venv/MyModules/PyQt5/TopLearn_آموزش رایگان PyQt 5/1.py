import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        self.winui()
        pass

    def winui(self):
        self.setWindowTitle("hello")
        self.resize(300, 400)

        self.menu = self.menuBar()
        self.file = self.menu.addMenu("File")

        #first
        self.new = QAction()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI()
    ui.show()
    # o = UI()
    # o.show()
    sys.exit(app.exec_())

# win = QMainWindow()
# win.setWindowTitle("hello")
# win.show()

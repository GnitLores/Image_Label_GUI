from re import A
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow
import sys


class ImageLabelGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_UI()

        window_pos_x, window_pos_y, window_width, window_height = 200, 200, 300, 300
        self.setGeometry(window_pos_x, window_pos_y, window_width, window_height)
        self.setWindowTitle("Image Label GUI")

    def init_UI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("Label Text")
        self.label.move(50, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click Me")
        self.b1.clicked.connect(self.clicked)

    def clicked(self):
        self.label.setText("You pressed the button!")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app = QApplication(sys.argv)
    win = ImageLabelGUI()

    win.show()
    sys.exit(app.exec())


window()

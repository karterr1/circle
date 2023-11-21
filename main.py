import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randrange, randint
from PyQt5.QtGui import QPainter, QColor
from view import Ui_Form


class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.run)
        self.a = False

    def run(self):
        self.a = True
        self.update()

    def paintEvent(self, event):
        if self.a:
            num = randrange(200)
            n = randrange(200)
            color = (randint(0, 255), randint(0, 255), randint(0, 255))
            painter = QPainter(self)
            painter.setBrush(QColor(*color))
            painter.drawEllipse(n, n, num, num)
            self.a = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from random import randrange

from Ui import Ui_Form


class CircleDrawer(QWidget, Ui_Form):
    CIRCLE_RADIUS = 50
    CIRCLES_NUMBER = 5
    BORDER = 5

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ellipses = []
        self.need_to_draw = False
        self.drawButton.clicked.connect(self.draw)

    def draw(self):
        self.need_to_draw = True
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_circles(qp)
        qp.end()

    def draw_circles(self, qp):
        width, height = self.width(), self.height()
        if self.need_to_draw:
            self.draw_last_circles(qp)
            for _ in range(self.CIRCLES_NUMBER):
                color = self.generate_color()
                qp.setBrush(color)
                x, y = randrange(self.CIRCLE_RADIUS + self.BORDER, width - self.CIRCLE_RADIUS * 2 - self.BORDER), \
                       randrange(self.CIRCLE_RADIUS + self.BORDER, height - self.CIRCLE_RADIUS * 2 - self.BORDER)
                qp.drawEllipse(x, y, self.CIRCLE_RADIUS * 2, self.CIRCLE_RADIUS * 2)
                self.ellipses.append((x, y, color))
            self.need_to_draw = False
        else:
            self.draw_last_circles(qp)

    def draw_last_circles(self, qp):
        for x, y, color in self.ellipses:
            qp.setBrush(color)
            qp.drawEllipse(x, y, self.CIRCLE_RADIUS * 2, self.CIRCLE_RADIUS * 2)

    def generate_color(self):
        return QColor(randrange(255), randrange(255), randrange(255))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CircleDrawer()
    window.show()
    sys.exit(app.exec())

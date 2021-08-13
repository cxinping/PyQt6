# -*- coding: utf-8 -*-

"""
    【简介】
	PySide6中 QScrollBar 例子

"""

from PySide6.QtWidgets import *
from PySide6 import QtGui, QtCore
from PySide6.QtGui import QPalette, QFont, QColor
import sys


class Example(QWidget):

    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        self.l1 = QLabel("拖动滑动条去改变颜色")
        self.l1.setFont(QFont("Arial", 16))
        hbox.addWidget(self.l1)
        self.s1 = QScrollBar()
        self.s1.setMaximum(255)
        self.s1.sliderMoved.connect(self.sliderval)
        self.s2 = QScrollBar()
        self.s2.setMaximum(255)
        self.s2.sliderMoved.connect(self.sliderval)
        self.s3 = QScrollBar()
        self.s3.setMaximum(255)
        self.s3.sliderMoved.connect(self.sliderval)
        hbox.addWidget(self.s1)
        hbox.addWidget(self.s2)
        hbox.addWidget(self.s3)
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QScrollBar 例子')
        self.setLayout(hbox)

    def sliderval(self):
        print(self.s1.value(), self.s2.value(), self.s3.value())
        # 设置调色板
        palette = QPalette()
        color = QColor(self.s1.value(), self.s2.value(), self.s3.value(), 255)
        palette.setColor(QPalette.WindowText, color)
        self.l1.setPalette(palette)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Example()
    demo.show()
    sys.exit(app.exec())

# -*- coding: utf-8 -*- 
"""
    【简介】
    PySide6中 QThread 例子


"""

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

global sec
sec = 0


def setTime():
    print('* setTime *')
    global sec
    sec += 1
    # LED显示数字+1
    lcdNumber.display(sec)


def work():
    print('* work ')
    # 计时器每秒计数
    timer.start(1000)
    for i in range(2000000000):
        pass

    #timer.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    top = QWidget()
    top.resize(300, 120)

    # 垂直布局类QVBoxLayout
    layout = QVBoxLayout(top)
    # 加个显示屏
    lcdNumber = QLCDNumber()
    layout.addWidget(lcdNumber)
    button = QPushButton("测试")
    layout.addWidget(button)

    timer = QTimer()
    # 每次计时结束，触发setTime
    timer.timeout.connect(setTime)
    button.clicked.connect(work)

    top.show()
    sys.exit(app.exec())

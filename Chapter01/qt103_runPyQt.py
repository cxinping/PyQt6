# -*- coding: utf-8 -*-
'''
【简介】
PyQT6的第一个简单例子
'''

import sys
from PyQt6.QtWidgets import QApplication, QWidget

app = QApplication(sys.argv)
window = QWidget()
window.resize(500, 500)
window.move(300, 300)
window.setWindowTitle('hello PyQt6')
window.show()
sys.exit(app.exec())

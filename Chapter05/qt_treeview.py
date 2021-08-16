#!/usr/bin/env python3

"""
    【简介】
	PySide6中 QTreeView 例子


"""

import sys
from PySide6.QtWidgets import QApplication, QTreeView, QFileSystemModel
from PySide6.QtCore import QDir
from PySide6.QtGui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Window系统提供的模式
    model = QFileSystemModel()

    # QFileSystemModel 只有设置了setRootPath后才会起作用。
    model.setRootPath('')
    # 创建一个QtreeView部件
    tree = QTreeView()
    # 为部件添加模式
    tree.setModel(model)
    tree.setWindowTitle("QTreeView 例子")
    tree.resize(500, 310)
    tree.show()
    sys.exit(app.exec())

# -*- coding: utf-8 -*-

"""
    【简介】
	PySide6中 QListView 例子

"""

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class ListViewDemo(QWidget):
    def __init__(self, parent=None):
        super(ListViewDemo, self).__init__(parent)
        self.setWindowTitle("QListView 例子")
        self.resize(270, 200)
        layout = QVBoxLayout()

        listView = QListView()
        slm = QStringListModel()
        self.qList = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5', 'Item 6']
        slm.setStringList(self.qList)
        listView.setModel(slm)
        listView.clicked.connect(self.clicked)
        layout.addWidget(listView)
        self.setLayout(layout)

    def clicked(self, qModelIndex):
        QMessageBox.information(self, "QListView", "你选择了: " + self.qList[qModelIndex.row()])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListViewDemo()
    win.show()
    sys.exit(app.exec())

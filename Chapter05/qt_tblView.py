# -*- coding: utf-8 -*- 
"""
    【简介】
	PySide6中 QTableView表格视图控件的例子

"""

from PySide6.QtWidgets import (QTableView, QApplication, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QMessageBox,
                               QAbstractItemView, QHeaderView)
from PySide6.QtGui import QStandardItemModel, QStandardItem
import sys
from PySide6.QtCore import Qt


class Table(QWidget):

    def __init__(self, arg=None):
        super(Table, self).__init__(arg)
        # 设置窗体的标题和初始大小
        self.setWindowTitle("QTableView表格视图控件的例子")
        self.resize(600, 300)

        # 准备数据模型，设置数据层次结构为6行5列
        self.model = QStandardItemModel(6, 5)
        # 设置数据栏名称
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4',  '标题5'])

        for row in range(6):
            for column in range(5):
                item = QStandardItem("行 %s, 列 %s" % (row, column ))
                self.model.setItem(row, column, item)

        # 实例化表格视图，设置模型为自定义的模型
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        ############ 下面代码让表格 100% 的填满窗口
        self.tableView.horizontalHeader().setStretchLastSection(True)
        self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 局部布局
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.tableView)
        # 全局布局
        wl = QVBoxLayout(self)
        wl.addLayout(vboxLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec())

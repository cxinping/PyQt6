# -*- coding: utf-8 -*- 
"""
    【简介】
	PySide6中QTableView表格视图控件的例子

"""

from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import sys


class Table(QWidget):

    def __init__(self, arg=None):
        super(Table, self).__init__(arg)
        self.setWindowTitle("QTableView表格视图控件的例子")
        self.resize(500, 300)
        self.model = QStandardItemModel(4, 4)
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4'])

        for row in range(4):
            for column in range(4):
                item = QStandardItem("row %s, column %s" % (row, column))
                self.model.setItem(row, column, item)

        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        # 下面代码让表格 100% 的填满窗口
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 下面代码可以选中表格的多行
        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        # self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置只能选中多行

        dlgLayout = QVBoxLayout()
        dlgLayout.addWidget(self.tableView)
        self.btn_1 = QPushButton("删除表格中选中的记录")
        self.btn_1.clicked.connect(self.btn_clicks_2)  # 连接点击信号到响应方法

        dlgLayout.addWidget(self.btn_1)

        self.setLayout(dlgLayout)

    # 点击响应方法, 删除当前选中的数据方法1
    def btn_clicks_1(self):
        print("点击了删除按钮")
        indexs = self.tableView.selectionModel().selection().indexes()
        if len(indexs) > 0:
            # 取第一行的索引
            index = indexs[0]
            self.model.removeRows(index.row(), 1)
        else:
            MessageBox = QMessageBox()
            MessageBox.information(self.tableView, "标题", "没有选中表格中要删除的行")

    # 点击响应方法, 删除当前选中的数据方法2
    def btn_clicks_2(self):
        print("点击了删除按钮")
        index = self.tableView.currentIndex()
        print(index,index.row())
        self.model.removeRow(index.row())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec())

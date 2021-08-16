# -*- coding: utf-8 -*- 
"""
    【简介】
	PySide6中 QTableView表格视图控件的例子

"""

from PySide6.QtWidgets import QTableView, QApplication, QHBoxLayout, QVBoxLayout, QWidget, QPushButton, QMessageBox, QAbstractItemView, QHeaderView
from PySide6.QtGui import QStandardItemModel,QStandardItem
import sys


class Table(QWidget):

    def __init__(self, arg=None):
        super(Table, self).__init__(arg)
        # 设置窗体的标题和初始大小
        self.setWindowTitle("QTableView表格视图控件的例子")
        self.resize(500, 300)

        # 设置数据层次结构，5行4列
        self.model = QStandardItemModel(5, 4)
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4'])

        for row in range(5):
            for column in range(4):
                item = QStandardItem("row %s, column %s" % (row, column))
                self.model.setItem(row, column, item)

        # 实例化表格视图，设置模型为自定义的模型
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        # 下面代码让表格 100% 的填满窗口
        # self.tableView.horizontalHeader().setStretchLastSection(True)
        # self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # 下面代码可以选中表格的多行
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置只能选中多行

        # 局部布局
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.tableView)
        self.add_btn = QPushButton("添加记录")
        self.add_btn.clicked.connect(self.add_records_btn_click)  # 连接点击信号到响应方法

        self.del_btn = QPushButton("删除选中的记录")
        self.del_btn.clicked.connect(self.del_records_btn_click)  # 连接点击信号到响应方法
        # 局部布局
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(self.add_btn)
        hboxLayout.addWidget(self.del_btn)

        # 全局布局
        wl = QVBoxLayout(self)
        wl.addLayout(vboxLayout)
        wl.addLayout(hboxLayout)


    # 点击响应方法, 删除当前选中的数据方法1
    def btn_clicks_1(self):
        indexs = self.tableView.selectionModel().selection().indexes()
        print(indexs)
        if len(indexs) > 0:
            # 取第一行的索引
            index = indexs[0]
            self.model.removeRows(index.row(), 1)

        else:
            MessageBox = QMessageBox()
            MessageBox.information(self.tableView, "标题", "没有选中表格中要删除的行")

    # 点击删除按钮响应方法, 删除选中的多行数据
    def del_records_btn_click(self):
        # index = self.tableView.currentIndex()
        # print(index, index.row())
        #self.model.removeRow(index.row())

        # indexs = self.tableView.selectionModel().selectedRows()
        # for index in reversed(indexs):
        #     self.model.removeRow(index.row())

        indexs = self.tableView.selectionModel().selectedRows()
        list1 = []  # 创建一个空list用于存放需要删除的行号
        for index in indexs:
            list1.append(index.row())  # 获得需要删除的行号的list
        list1.sort(key=int, reverse=True)  # 用sort方法将list进行降序排列
        for i in list1:  # 按照list删除对应行
            self.model.removeRow(i)

    # 点击添加按钮相应方法，添加数据
    def add_records_btn_click(self):
        self.model.appendRow([
            QStandardItem("row %s, column %s" % (5, 0)),
            QStandardItem("row %s, column %s" % (6, 1)),
            QStandardItem("row %s, column %s" % (7, 2)),
            QStandardItem("row %s, column %s" % (8, 3)),
        ])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    table = Table()
    table.show()
    sys.exit(app.exec())

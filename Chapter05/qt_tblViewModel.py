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
        self.resize(500, 300)

        # 准备数据模型，设置数据层次结构为5行4列
        self.model = QStandardItemModel(5, 4)
        # 设置数据栏名称
        self.model.setHorizontalHeaderLabels(['标题1', '标题2', '标题3', '标题4'])

        for row in range(5):
            for column in range(4):
                item = QStandardItem("row %s, column %s" % (row, column))
                self.model.setItem(row, column, item)

        # 实例化表格视图，设置模型为自定义的模型
        self.tableView = QTableView()
        self.tableView.setModel(self.model)

        ############ 下面代码让表格 100% 的填满窗口
        #self.tableView.horizontalHeader().setStretchLastSection(True)
        #self.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        ############ 下面代码要限定只能选择整行
        # self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        # self.tableView.setSelectionMode(QAbstractItemView.SingleSelection)  # 设置只能选中一行

        ############# 下面代码可以选中表格的多行
        self.tableView.setSelectionBehavior(QAbstractItemView.SelectRows)  # 设置只能选中整行
        self.tableView.setSelectionMode(QAbstractItemView.ExtendedSelection)  # 设置只能选中多行

        # 让 tableView 失去焦点
        self.tableView.setFocusPolicy(Qt.NoFocus)
        
        # 去掉左边的行号
        # headerView  = self.tableView.verticalHeader()
        # headerView.setHidden(True)

        # 局部布局
        vboxLayout = QVBoxLayout()
        vboxLayout.addWidget(self.tableView)
        self.add_btn = QPushButton("添加记录")
        # 连接信号槽，点击按钮 add_bt n绑定槽事件
        self.add_btn.clicked.connect(self.add_records_btn_click)

        self.del_btn = QPushButton("删除多行记录")
        # 连接信号槽，点击按钮 del_btn 绑定槽事件
        self.del_btn.clicked.connect(self.del_record_btn_click)
        # 局部布局
        hboxLayout = QHBoxLayout()
        hboxLayout.addWidget(self.add_btn)
        hboxLayout.addWidget(self.del_btn)

        # 全局布局
        wl = QVBoxLayout(self)
        wl.addLayout(vboxLayout)
        wl.addLayout(hboxLayout)

    # 点击删除按钮响应方法, 删除选中的单行数据
    def del_record_btn_click(self):
        # 第一种方法: 删除单行数据
        # indexs = self.tableView.selectionModel().selection().indexes()
        # if len(indexs) > 0:
        #     # 取第一行的索引
        #     index = indexs[0]
        #     self.model.removeRows(index.row(), 1)

        # 第二种方法: 删除单行数据
        index = self.tableView.currentIndex()  # 取得当前选中行的index
        if -1 == index.row():
            return
        print(index.row())
        self.model.removeRow(index.row())  # 通过index的row()操作得到行数进行删除

    # 点击删除按钮响应方法, 删除选中的多行数据
    def del_records_btn_click(self):
        indexs = self.tableView.selectionModel().selection().indexes()
        #print(indexs)
        temp_list = []
        for index in reversed(indexs):
            #print('index.row() => ',index.row())
            temp_list.append(index.row())
            #self.model.removeRow(index.row())

        temp_list.sort(key=int, reverse=True)
        print(temp_list)

        # indexs = self.tableView.selectionModel().selectedRows()
        # temp_list = []  # 创建一个空队列用于存放需要删除的行号
        # for index in indexs:
        #     temp_list.append(index.row())  # 队列中保存需要删除的行号
        # temp_list.sort(key=int, reverse=True)  # 用sort方法将队列进行降序排列
        # print(temp_list)
        # if temp_list:
        #     for i in temp_list:  # 按照队列删除对应的行
        #         self.model.removeRow(i)
        # else:
        #     MessageBox = QMessageBox()
        #     MessageBox.information(self.tableView, "标题", "没有选中表格中要删除的行")

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

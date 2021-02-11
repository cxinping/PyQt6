# -*- coding: utf-8 -*- 
'''
    【简介】
	保存PyQt6类的使用手册到本地
   
    
'''

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import QWidget

out = sys.stdout
sys.stdout = open(r'E:\QWidget.txt', 'w')
help( QWidget  )
sys.stdout.close()
sys.stdout = out

import sys 	
from PyQt6 import QtWidgets

'''
【简介】
第一个PyQt6例子    
'''

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("hello, pyqt6")
widget.show()
sys.exit(app.exec())

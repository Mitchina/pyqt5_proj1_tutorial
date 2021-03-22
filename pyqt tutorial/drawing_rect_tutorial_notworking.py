# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'changing_images_designer.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
# QPixmap only works with absolute Path
# add os.path.dirname(__file__) and then join it with the path of the folder and the image
import os
# drawing
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        # image size rectangle
        self.label.setGeometry(QtCore.QRect(0, 0, 831, 451))
        self.label.setText("")
        self.FILEPATH = os.path.dirname(__file__)
        self.IMG1 = "assets\\deep_sea_2d_1.jpg"
        self.IMG2 = "assets\\deep_sea_2d_2.jpg"
        self.IMG3 = "assets\\deep_sea_2d_3.jpeg"
        self.IMG4 = "assets\\deep_sea_2d_4.png"
        print(self.FILEPATH)
        # copy that line bellow, to change the photo when we click the buttons
        self.label.setPixmap(QtGui.QPixmap(os.path.join(self.FILEPATH , self.IMG1))) # use os.path.join to join the path and the folder
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        
        self.button1 = QtWidgets.QPushButton(self.centralwidget)
        self.button1.setGeometry(QtCore.QRect(100, 470, 121, 51))
        self.button1.setObjectName("button1")
        self.button4 = QtWidgets.QPushButton(self.centralwidget)
        self.button4.setGeometry(QtCore.QRect(580, 470, 121, 51))
        self.button4.setObjectName("button4")
        self.button2 = QtWidgets.QPushButton(self.centralwidget)
        self.button2.setGeometry(QtCore.QRect(260, 470, 121, 51))
        self.button2.setObjectName("button2")
        self.button3 = QtWidgets.QPushButton(self.centralwidget)
        self.button3.setGeometry(QtCore.QRect(420, 470, 121, 51))
        self.button3.setObjectName("button3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # link our buttons with those pic methods
        self.button1.clicked.connect(self.show_pic1)
        self.button2.clicked.connect(self.show_pic2)
        self.button3.clicked.connect(self.show_pic3)
        self.button4.clicked.connect(self.show_pic4)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Drawing Rectangles"))
        
        self.button1.setText(_translate("MainWindow", "1"))
        self.button4.setText(_translate("MainWindow", "4"))
        self.button2.setText(_translate("MainWindow", "2"))
        self.button3.setText(_translate("MainWindow", "3"))

    # creating some methods that will show a different picture for each button
    def show_pic1(self):
        # paste the line where I've the photo here
        self.label.setPixmap(QtGui.QPixmap(os.path.join(self.FILEPATH , self.IMG1)))             

    def show_pic2(self):
        self.label.setPixmap(QtGui.QPixmap(os.path.join(self.FILEPATH , self.IMG2)))
    
    def show_pic3(self):
        self.label.setPixmap(QtGui.QPixmap(os.path.join(self.FILEPATH , self.IMG3)))
    
    def show_pic4(self):
        self.label.setPixmap(QtGui.QPixmap(os.path.join(self.FILEPATH , self.IMG4)))
    
    # defining a paint event, passing an event 'e'
    def paintEvent(self, e):
        self.COLOR_LAYER1 - "#a5ffe7"
        self.COLOR_LAYER2 - "#a5e1e7"
        self.COLOR_LAYER3 - "#75c8dc"
        self.COLOR_LAYER4 - "#41b2dc"
        self.COLOR_LAYER5 - "#1d9af2"
        self.COLOR_LAYER6 - "#0078f2"
        self.COLOR_LAYER7 - "#005df2"
        self.COLOR_LAYER8 - "#093aff"
        self.COLOR_LAYER9 - "#091bff"
        self.COLOR_LAYER10 - "#08306b"
        self.COLOR_LAYER11 - "#0400c6"

        # creating a painter object
        painter = QPainter(self)
        # color and pen size
        painter.setPen(QPen(QColor("#0400c6"), 5, Qt.SolidLine))

        # fill with color
        painter.setBrush(QBrush(QColor("#0400c6"), Qt.SolidPattern))

        # draw on top of the image. using the size of the image (label) and the image itself
        painter.drawPixmap(QtCore.QRect(0, 0, 831, 451), self.IMG1)

        # draw rectangle, xy position, width and height
        painter.drawRect(50, 50, 100, 50)
        print(painter)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
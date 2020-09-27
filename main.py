# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMessageBox


import database



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 120, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        
        
        self.ac = QtWidgets.QLineEdit(self.centralwidget)
        self.ac.setGeometry(QtCore.QRect(190, 170, 441, 22))
        self.ac.setObjectName("ac")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 170, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(190, 210, 311, 22))
        self.name.setObjectName("name")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(110, 200, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.amt = QtWidgets.QLineEdit(self.centralwidget)
        self.amt.setGeometry(QtCore.QRect(190, 250, 311, 22))
        self.amt.setObjectName("amt")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 250, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 290, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.date = QtWidgets.QDateEdit(self.centralwidget)
        self.date.setGeometry(QtCore.QRect(190, 290, 241, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.date.setFont(font)
        self.date.setObjectName("date")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(270, 360, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.submit.clicked.connect(self.add)
        #self.submit.clicked.connect(self.popup)

    def add(self):
        
        nm = self.name.text()
        amunt = int(self.amt.text())
        acno = int(self.ac.text())
        dt = self.date.text()

        x = database.addtodb(acno,nm,amunt,dt)

        if x == "yes":
            Ui_MainWindow.setupUi(self, MainWindow)
            Ui_MainWindow.retranslateUi(self, MainWindow)

    #def popup(self):

     #   msg = QMessageBox()
     #   uid = database.maxid()
     #   msg.setWindowTitle("Unique ID")
     #   msg.setText(f"Unique ID is {uid}")

     #   x1 = msg.exec_() 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.label_2.setText(_translate("MainWindow", "A/C NO"))
        self.label_3.setText(_translate("MainWindow", "Name"))
        self.label_4.setText(_translate("MainWindow", "Amount"))
        self.label_5.setText(_translate("MainWindow", "Date"))
        self.submit.setText(_translate("MainWindow", "SUBMIT"))
        self.date.setDisplayFormat(_translate("MainWindow", "yyyy-MM-dd"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

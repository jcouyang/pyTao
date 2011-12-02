# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUi.ui'
#
# Created: Fri Nov 25 13:51:51 2011
#      by: pyside-uic 0.2.13 running on PySide 1.0.7
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(675, 473)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.loginBtn = QtGui.QPushButton(self.centralwidget)
        self.loginBtn.setGeometry(QtCore.QRect(520, 60, 141, 32))
        self.loginBtn.setObjectName("loginBtn")
        self.scanBtn = QtGui.QPushButton(self.centralwidget)
        self.scanBtn.setGeometry(QtCore.QRect(520, 260, 141, 91))
        self.scanBtn.setObjectName("scanBtn")
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 501, 191))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.InfoTabWidget = QtGui.QTabWidget(self.centralwidget)
        self.InfoTabWidget.setGeometry(QtCore.QRect(10, 250, 501, 181))
        self.InfoTabWidget.setObjectName("InfoTabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.listWidget = QtGui.QListWidget(self.tab)
        self.listWidget.setGeometry(QtCore.QRect(0, 0, 501, 151))
        self.listWidget.setObjectName("listWidget")
        self.InfoTabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidget_2 = QtGui.QListWidget(self.tab_2)
        self.listWidget_2.setGeometry(QtCore.QRect(0, 0, 501, 151))
        self.listWidget_2.setObjectName("listWidget_2")
        self.InfoTabWidget.addTab(self.tab_2, "")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 111, 16))
        self.label.setObjectName("label")
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(520, 360, 141, 71))
        self.pushButton.setObjectName("pushButton")
        self.company = QtGui.QComboBox(self.centralwidget)
        self.company.setGeometry(QtCore.QRect(450, 10, 211, 21))
        self.company.setObjectName("company")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar()
        self.menubar.setGeometry(QtCore.QRect(0, 0, 675, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        self.InfoTabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.loginBtn.setText(QtGui.QApplication.translate("MainWindow", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.scanBtn.setText(QtGui.QApplication.translate("MainWindow", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.InfoTabWidget.setTabText(self.InfoTabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "Location Info", None, QtGui.QApplication.UnicodeUTF8))
        self.InfoTabWidget.setTabText(self.InfoTabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Items Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Items to be Send", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Sent", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))


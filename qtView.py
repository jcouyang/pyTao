#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import sys
from PySide.QtCore import *
from PySide.QtGui import *
from mainUi import*
from login import*
from taobaoapi2 import *

def login(self):
    print 'login'
    loginDialog = LoginDialog()
    loginDialog.exec_()
    
def getSoldItem(*args):
    # Taobao bussinuss
    itemSold = TradesSoldGet()
    itemSold.setParams(session=sessionKey.get(),status='WAIT_SELLER_SEND_GOODS')
    itemSold.fetch()
    return itemSold.datas

def getCompany(*args):
    deliveryCompany = CompaniesGet()
    deliveryCompany.fetch()

    return deliveryCompany.datas

class LoginDialog(QDialog,Ui_Dialog):
    def __init__(self, parent=None):
        super(LoginDialog, self).__init__(parent)
        # Create widgets
        self.setupUi(self)
        self.webView.load(QUrl('file:///Users/ouyangjichao/Downloads/sharebookfree.com_1198292985/readme.txt'))
        

class MainUi(QMainWindow,Ui_MainWindow):
    sessionkey = ''
    def __init__(self, parent=None):
        super(MainUi, self).__init__(parent)
        # Create widgets
        self.setupUi(self)
        self.loginBtn.clicked.connect(login)
        self.scanBtn
    # Greets the user
    def greetings(self):
        print ("Hello %s" % self.edit.text())       
 
 
if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    mainUi = MainUi()
    mainUi.show()
    # loginDialog = LoginDialog()
    # loginDialog.show()
    # Run the main Qt loop
    sys.exit(app.exec_())


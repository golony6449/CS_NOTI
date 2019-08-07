# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cs_noti.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(646, 487)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 30, 571, 391))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.agencyLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.agencyLabel.setObjectName("agencyLabel")
        self.gridLayout.addWidget(self.agencyLabel, 2, 0, 1, 1)
        self.gnuLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.gnuLabel.setObjectName("gnuLabel")
        self.gridLayout.addWidget(self.gnuLabel, 1, 0, 1, 1)
        self.gnuBTN = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.gnuBTN.setObjectName("gnuBTN")
        self.gridLayout.addWidget(self.gnuBTN, 1, 2, 1, 1)
        self.csBTN = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.csBTN.setObjectName("csBTN")
        self.gridLayout.addWidget(self.csBTN, 0, 2, 1, 1)
        self.csLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.csLabel.setObjectName("csLabel")
        self.gridLayout.addWidget(self.csLabel, 0, 0, 1, 1)
        self.agencyBTN = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.agencyBTN.setObjectName("agencyBTN")
        self.gridLayout.addWidget(self.agencyBTN, 2, 2, 1, 1)
        self.gnuStatus = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.gnuStatus.setText("")
        self.gnuStatus.setObjectName("gnuStatus")
        self.gridLayout.addWidget(self.gnuStatus, 1, 1, 1, 1)
        self.csStatus = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.csStatus.setText("")
        self.csStatus.setObjectName("csStatus")
        self.gridLayout.addWidget(self.csStatus, 0, 1, 1, 1)
        self.agencyStatus = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.agencyStatus.setText("")
        self.agencyStatus.setObjectName("agencyStatus")
        self.gridLayout.addWidget(self.agencyStatus, 2, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 646, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSetting = QtWidgets.QAction(MainWindow)
        self.actionSetting.setObjectName("actionSetting")
        self.menu.addAction(self.actionSetting)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GNU_Notifier"))
        self.agencyLabel.setText(_translate("MainWindow", "Agency Notifier"))
        self.gnuLabel.setText(_translate("MainWindow", "GNU Notifier"))
        self.gnuBTN.setStatusTip(_translate("MainWindow", "HOT NEWS 공지사항"))
        self.gnuBTN.setText(_translate("MainWindow", "실행"))
        self.csBTN.setStatusTip(_translate("MainWindow", "컴퓨터과학과 공지사항"))
        self.csBTN.setText(_translate("MainWindow", "실행"))
        self.csLabel.setText(_translate("MainWindow", "CS Notifier"))
        self.agencyBTN.setStatusTip(_translate("MainWindow", "기관공지"))
        self.agencyBTN.setText(_translate("MainWindow", "실행"))
        self.menu.setTitle(_translate("MainWindow", "설정"))
        self.actionSetting.setText(_translate("MainWindow", "설정"))


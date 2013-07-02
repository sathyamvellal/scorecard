# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created: Tue Jul  2 21:41:36 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(380, 177)
        Form.setMouseTracking(True)
        Form.setAcceptDrops(True)
        Form.setAutoFillBackground(True)
        self.score = QtGui.QLabel(Form)
        self.score.setGeometry(QtCore.QRect(30, 70, 331, 51))
        self.score.setText(_fromUtf8(""))
        self.score.setObjectName(_fromUtf8("score"))
        self.refresh = QtGui.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(120, 140, 121, 31))
        self.refresh.setObjectName(_fromUtf8("refresh"))
        self.matchNo = QtGui.QTextEdit(Form)
        self.matchNo.setGeometry(QtCore.QRect(110, 10, 151, 41))
        self.matchNo.setObjectName(_fromUtf8("matchNo"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Score App", None, QtGui.QApplication.UnicodeUTF8))
        self.refresh.setText(QtGui.QApplication.translate("Form", "Refresh", None, QtGui.QApplication.UnicodeUTF8))


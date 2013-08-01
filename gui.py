# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'score.ui'
#
# Created: Thu Aug  1 20:40:41 2013
#      by: PyQt4 UI code generator 4.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(386, 177)
        Form.setMouseTracking(True)
        Form.setAcceptDrops(True)
        Form.setAutoFillBackground(True)
        self.score = QtGui.QLabel(Form)
        self.score.setGeometry(QtCore.QRect(20, 70, 341, 51))
        self.score.setText(_fromUtf8(""))
        self.score.setObjectName(_fromUtf8("score"))
        self.refresh = QtGui.QPushButton(Form)
        self.refresh.setGeometry(QtCore.QRect(100, 140, 161, 31))
        self.refresh.setObjectName(_fromUtf8("refresh"))
        self.scoreurl = QtGui.QTextEdit(Form)
        self.scoreurl.setGeometry(QtCore.QRect(20, 10, 341, 41))
        self.scoreurl.setObjectName(_fromUtf8("scoreurl"))
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 70, 341, 51))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Cricinfo Score App", None))
        self.refresh.setText(_translate("Form", "Get Score / Refresh", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


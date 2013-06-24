#!/usr/bin/python

from PyQt4 import QtGui, QtCore
from gui import Ui_Form
import sys
import os
import urllib

class Score(QtGui.QMainWindow):
	def __init__(self):
		super(Score, self).__init__()
		QtGui.QMainWindow.__init__(self, None, QtCore.Qt.WindowStaysOnTopHint)
		self.ui = Ui_Form()
		self.ui.setupUi(self)
		self.ui.refresh.clicked.connect(self.refresh)
		handle = urllib.urlopen("http://www.espncricinfo.com/icc-champions-trophy-2013/engine/current/match/566948.html")
		content = handle.read()
		page = content.split("<div class=\"topFrameTitle\">", 2)
		page2 = page[1].split("</div>")
		page3 = page2[0].split("data-text=\"")
		page4 = page3[1].split("\">Tweet")
		self.ui.score.setText(page4[0])
		self.move(1650, 30)
		self.show()

	def refresh(self):
		handle = urllib.urlopen("http://www.espncricinfo.com/icc-champions-trophy-2013/engine/current/match/566948.html")
		content = handle.read()
		page = content.split("<div class=\"topFrameTitle\">", 2)
		page2 = page[1].split("</div>")
		page3 = page2[0].split("data-text=\"")
		page4 = page3[1].split("\">Tweet")
		self.ui.score.setText(page4[0])

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	o = Score()
	sys.exit(app.exec_())

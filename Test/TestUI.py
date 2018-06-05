# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TestUI.ui'
#
# Created: Tue Jun 05 19:52:46 2018
#      by: PyQt4 UI code generator 4.11.3
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
        Form.resize(400, 300)
        self.TextBroser = QtGui.QTextBrowser(Form)
        self.TextBroser.setGeometry(QtCore.QRect(80, 90, 161, 192))
        self.TextBroser.setObjectName(_fromUtf8("TextBroser"))
        self.StartButton = QtGui.QPushButton(Form)
        self.StartButton.setGeometry(QtCore.QRect(30, 40, 93, 28))
        self.StartButton.setObjectName(_fromUtf8("StartButton"))
        self.StopButton = QtGui.QPushButton(Form)
        self.StopButton.setGeometry(QtCore.QRect(160, 40, 93, 28))
        self.StopButton.setObjectName(_fromUtf8("StopButton"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.StartButton.setText(_translate("Form", "start", None))
        self.StopButton.setText(_translate("Form", "stop", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


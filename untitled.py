# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Mon Jun 04 14:16:00 2018
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
        Form.resize(884, 828)
        self.portchoose_t = QtGui.QLabel(Form)
        self.portchoose_t.setGeometry(QtCore.QRect(20, 50, 72, 15))
        self.portchoose_t.setObjectName(_fromUtf8("portchoose_t"))
        self.baudratelchoose = QtGui.QComboBox(Form)
        self.baudratelchoose.setGeometry(QtCore.QRect(90, 90, 91, 21))
        self.baudratelchoose.setObjectName(_fromUtf8("baudratelchoose"))
        self.baudratelchoose.addItem(_fromUtf8(""))
        self.baudratelchoose.addItem(_fromUtf8(""))
        self.baudratelchoose.addItem(_fromUtf8(""))
        self.baudratelchoose.addItem(_fromUtf8(""))
        self.comchoose = QtGui.QComboBox(Form)
        self.comchoose.setGeometry(QtCore.QRect(90, 50, 91, 21))
        self.comchoose.setObjectName(_fromUtf8("comchoose"))
        self.baundrate_t = QtGui.QLabel(Form)
        self.baundrate_t.setGeometry(QtCore.QRect(20, 90, 72, 15))
        self.baundrate_t.setObjectName(_fromUtf8("baundrate_t"))
        self.stop_t = QtGui.QLabel(Form)
        self.stop_t.setGeometry(QtCore.QRect(20, 130, 72, 15))
        self.stop_t.setObjectName(_fromUtf8("stop_t"))
        self.comboBox = QtGui.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(90, 130, 87, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.data_t = QtGui.QLabel(Form)
        self.data_t.setGeometry(QtCore.QRect(20, 180, 72, 15))
        self.data_t.setObjectName(_fromUtf8("data_t"))
        self.datachoose = QtGui.QComboBox(Form)
        self.datachoose.setGeometry(QtCore.QRect(90, 180, 87, 22))
        self.datachoose.setObjectName(_fromUtf8("datachoose"))
        self.datachoose.addItem(_fromUtf8(""))
        self.datachoose.addItem(_fromUtf8(""))
        self.datachoose.addItem(_fromUtf8(""))
        self.datachoose.addItem(_fromUtf8(""))
        self.check_t = QtGui.QLabel(Form)
        self.check_t.setGeometry(QtCore.QRect(10, 230, 72, 15))
        self.check_t.setObjectName(_fromUtf8("check_t"))
        self.checkchoose = QtGui.QComboBox(Form)
        self.checkchoose.setGeometry(QtCore.QRect(90, 230, 87, 22))
        self.checkchoose.setObjectName(_fromUtf8("checkchoose"))
        self.checkchoose.addItem(_fromUtf8(""))
        self.checkchoose.addItem(_fromUtf8(""))
        self.checkchoose.addItem(_fromUtf8(""))
        self.portopet_t = QtGui.QLabel(Form)
        self.portopet_t.setGeometry(QtCore.QRect(10, 280, 72, 15))
        self.portopet_t.setObjectName(_fromUtf8("portopet_t"))
        self.portoperate = QtGui.QPushButton(Form)
        self.portoperate.setGeometry(QtCore.QRect(90, 270, 93, 28))
        self.portoperate.setObjectName(_fromUtf8("portoperate"))
        self.lineEditCommand = QtGui.QLineEdit(Form)
        self.lineEditCommand.setGeometry(QtCore.QRect(10, 490, 721, 161))
        self.lineEditCommand.setObjectName(_fromUtf8("lineEditCommand"))
        self.textEdit_show = QtGui.QTextEdit(Form)
        self.textEdit_show.setGeometry(QtCore.QRect(220, 50, 631, 421))
        self.textEdit_show.setObjectName(_fromUtf8("textEdit_show"))
        self.saveInfo = QtGui.QPushButton(Form)
        self.saveInfo.setGeometry(QtCore.QRect(10, 330, 93, 28))
        self.saveInfo.setObjectName(_fromUtf8("saveInfo"))
        self.clearInfo = QtGui.QPushButton(Form)
        self.clearInfo.setGeometry(QtCore.QRect(120, 330, 93, 28))
        self.clearInfo.setObjectName(_fromUtf8("clearInfo"))
        self.Time = QtGui.QCheckBox(Form)
        self.Time.setGeometry(QtCore.QRect(10, 380, 91, 19))
        self.Time.setObjectName(_fromUtf8("Time"))
        self.inFoSend = QtGui.QPushButton(Form)
        self.inFoSend.setGeometry(QtCore.QRect(750, 520, 93, 28))
        self.inFoSend.setObjectName(_fromUtf8("inFoSend"))
        self.InfoClear = QtGui.QPushButton(Form)
        self.InfoClear.setGeometry(QtCore.QRect(750, 580, 93, 28))
        self.InfoClear.setObjectName(_fromUtf8("InfoClear"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.portchoose_t.setText(_translate("Form", "串口选择", None))
        self.baudratelchoose.setItemText(0, _translate("Form", "921600", None))
        self.baudratelchoose.setItemText(1, _translate("Form", "115200", None))
        self.baudratelchoose.setItemText(2, _translate("Form", "74880", None))
        self.baudratelchoose.setItemText(3, _translate("Form", "Custom", None))
        self.baundrate_t.setText(_translate("Form", "波特率", None))
        self.stop_t.setText(_translate("Form", "停止位", None))
        self.comboBox.setItemText(0, _translate("Form", "1", None))
        self.comboBox.setItemText(1, _translate("Form", "1.5", None))
        self.comboBox.setItemText(2, _translate("Form", "2", None))
        self.data_t.setText(_translate("Form", "数据位", None))
        self.datachoose.setItemText(0, _translate("Form", "8", None))
        self.datachoose.setItemText(1, _translate("Form", "7", None))
        self.datachoose.setItemText(2, _translate("Form", "6", None))
        self.datachoose.setItemText(3, _translate("Form", "5", None))
        self.check_t.setText(_translate("Form", "奇偶校验", None))
        self.checkchoose.setItemText(0, _translate("Form", "无", None))
        self.checkchoose.setItemText(1, _translate("Form", "奇校验", None))
        self.checkchoose.setItemText(2, _translate("Form", "偶校验", None))
        self.portopet_t.setText(_translate("Form", "串口操作", None))
        self.portoperate.setText(_translate("Form", "close", None))
        self.saveInfo.setText(_translate("Form", "保存窗口", None))
        self.clearInfo.setText(_translate("Form", "PushButton", None))
        self.Time.setText(_translate("Form", "时间撮", None))
        self.inFoSend.setText(_translate("Form", "发送", None))
        self.InfoClear.setText(_translate("Form", "清除发送", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())


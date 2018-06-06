# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SerialToolUI.ui'
#
# Created: Wed Jun 06 09:39:06 2018
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

class Ui_Espressif(object):
    def setupUi(self, Espressif):
        Espressif.setObjectName(_fromUtf8("Espressif"))
        Espressif.resize(865, 768)
        self.portchoose_t = QtGui.QLabel(Espressif)
        self.portchoose_t.setGeometry(QtCore.QRect(20, 50, 72, 15))
        self.portchoose_t.setObjectName(_fromUtf8("portchoose_t"))
        self.baudratelchoose = QtGui.QComboBox(Espressif)
        self.baudratelchoose.setEnabled(True)
        self.baudratelchoose.setGeometry(QtCore.QRect(90, 90, 91, 21))
        self.baudratelchoose.setObjectName(_fromUtf8("baudratelchoose"))
        self.baudratelchoose.addItem(_fromUtf8(""))
        self.baudratelchoose.addItem(_fromUtf8(""))
        self.baudratelchoose.addItem(_fromUtf8(""))
        self.comchoose = QtGui.QComboBox(Espressif)
        self.comchoose.setGeometry(QtCore.QRect(90, 50, 91, 21))
        self.comchoose.setObjectName(_fromUtf8("comchoose"))
        self.baundrate_t = QtGui.QLabel(Espressif)
        self.baundrate_t.setGeometry(QtCore.QRect(20, 90, 72, 15))
        self.baundrate_t.setObjectName(_fromUtf8("baundrate_t"))
        self.stop_t = QtGui.QLabel(Espressif)
        self.stop_t.setGeometry(QtCore.QRect(20, 130, 72, 15))
        self.stop_t.setObjectName(_fromUtf8("stop_t"))
        self.stopChoose = QtGui.QComboBox(Espressif)
        self.stopChoose.setGeometry(QtCore.QRect(90, 130, 87, 22))
        self.stopChoose.setObjectName(_fromUtf8("stopChoose"))
        self.stopChoose.addItem(_fromUtf8(""))
        self.stopChoose.addItem(_fromUtf8(""))
        self.stopChoose.addItem(_fromUtf8(""))
        self.data_t = QtGui.QLabel(Espressif)
        self.data_t.setGeometry(QtCore.QRect(20, 180, 72, 15))
        self.data_t.setObjectName(_fromUtf8("data_t"))
        self.datachoose = QtGui.QComboBox(Espressif)
        self.datachoose.setGeometry(QtCore.QRect(90, 180, 87, 22))
        self.datachoose.setObjectName(_fromUtf8("datachoose"))
        self.datachoose.addItem(_fromUtf8(""))
        self.datachoose.addItem(_fromUtf8(""))
        self.datachoose.addItem(_fromUtf8(""))
        self.datachoose.addItem(_fromUtf8(""))
        self.check_t = QtGui.QLabel(Espressif)
        self.check_t.setGeometry(QtCore.QRect(10, 230, 72, 15))
        self.check_t.setObjectName(_fromUtf8("check_t"))
        self.checkchoose = QtGui.QComboBox(Espressif)
        self.checkchoose.setGeometry(QtCore.QRect(90, 230, 87, 22))
        self.checkchoose.setObjectName(_fromUtf8("checkchoose"))
        self.checkchoose.addItem(_fromUtf8(""))
        self.checkchoose.addItem(_fromUtf8(""))
        self.checkchoose.addItem(_fromUtf8(""))
        self.portopet_t = QtGui.QLabel(Espressif)
        self.portopet_t.setGeometry(QtCore.QRect(10, 280, 72, 15))
        self.portopet_t.setObjectName(_fromUtf8("portopet_t"))
        self.portoperate = QtGui.QPushButton(Espressif)
        self.portoperate.setGeometry(QtCore.QRect(90, 270, 93, 28))
        self.portoperate.setObjectName(_fromUtf8("portoperate"))
        self.lineEditCommand = QtGui.QLineEdit(Espressif)
        self.lineEditCommand.setGeometry(QtCore.QRect(10, 490, 721, 161))
        self.lineEditCommand.setObjectName(_fromUtf8("lineEditCommand"))
        self.saveInfo = QtGui.QPushButton(Espressif)
        self.saveInfo.setGeometry(QtCore.QRect(10, 330, 93, 28))
        self.saveInfo.setObjectName(_fromUtf8("saveInfo"))
        self.clearInfo = QtGui.QPushButton(Espressif)
        self.clearInfo.setGeometry(QtCore.QRect(120, 330, 93, 28))
        self.clearInfo.setObjectName(_fromUtf8("clearInfo"))
        self.Time = QtGui.QCheckBox(Espressif)
        self.Time.setGeometry(QtCore.QRect(10, 380, 91, 19))
        self.Time.setObjectName(_fromUtf8("Time"))
        self.inFoSend = QtGui.QPushButton(Espressif)
        self.inFoSend.setGeometry(QtCore.QRect(750, 490, 93, 28))
        self.inFoSend.setObjectName(_fromUtf8("inFoSend"))
        self.InfoClear = QtGui.QPushButton(Espressif)
        self.InfoClear.setGeometry(QtCore.QRect(750, 550, 93, 28))
        self.InfoClear.setObjectName(_fromUtf8("InfoClear"))
        self.baudEdit = QtGui.QLineEdit(Espressif)
        self.baudEdit.setEnabled(True)
        self.baudEdit.setGeometry(QtCore.QRect(180, 20, 71, 21))
        self.baudEdit.setReadOnly(False)
        self.baudEdit.setObjectName(_fromUtf8("baudEdit"))
        self.SendNewLine = QtGui.QCheckBox(Espressif)
        self.SendNewLine.setGeometry(QtCore.QRect(750, 610, 91, 19))
        self.SendNewLine.setObjectName(_fromUtf8("SendNewLine"))
        self.InfoBrower = QtGui.QTextBrowser(Espressif)
        self.InfoBrower.setGeometry(QtCore.QRect(240, 50, 621, 381))
        self.InfoBrower.setObjectName(_fromUtf8("InfoBrower"))

        self.retranslateUi(Espressif)
        QtCore.QMetaObject.connectSlotsByName(Espressif)

    def retranslateUi(self, Espressif):
        Espressif.setWindowTitle(_translate("Espressif", "Form", None))
        self.portchoose_t.setText(_translate("Espressif", "串口选择", None))
        self.baudratelchoose.setItemText(0, _translate("Espressif", "921600", None))
        self.baudratelchoose.setItemText(1, _translate("Espressif", "115200", None))
        self.baudratelchoose.setItemText(2, _translate("Espressif", "74880", None))
        self.baundrate_t.setText(_translate("Espressif", "波特率", None))
        self.stop_t.setText(_translate("Espressif", "停止位", None))
        self.stopChoose.setItemText(0, _translate("Espressif", "1", None))
        self.stopChoose.setItemText(1, _translate("Espressif", "1.5", None))
        self.stopChoose.setItemText(2, _translate("Espressif", "2", None))
        self.data_t.setText(_translate("Espressif", "数据位", None))
        self.datachoose.setItemText(0, _translate("Espressif", "8", None))
        self.datachoose.setItemText(1, _translate("Espressif", "7", None))
        self.datachoose.setItemText(2, _translate("Espressif", "6", None))
        self.datachoose.setItemText(3, _translate("Espressif", "5", None))
        self.check_t.setText(_translate("Espressif", "奇偶校验", None))
        self.checkchoose.setItemText(0, _translate("Espressif", "无", None))
        self.checkchoose.setItemText(1, _translate("Espressif", "奇校验", None))
        self.checkchoose.setItemText(2, _translate("Espressif", "偶校验", None))
        self.portopet_t.setText(_translate("Espressif", "串口操作", None))
        self.portoperate.setText(_translate("Espressif", "close", None))
        self.saveInfo.setText(_translate("Espressif", "保存窗口", None))
        self.clearInfo.setText(_translate("Espressif", "清除窗口", None))
        self.Time.setText(_translate("Espressif", "时间撮", None))
        self.inFoSend.setText(_translate("Espressif", "发送", None))
        self.InfoClear.setText(_translate("Espressif", "清除发送", None))
        self.SendNewLine.setText(_translate("Espressif", "发送新行", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Espressif = QtGui.QWidget()
    ui = Ui_Espressif()
    ui.setupUi(Espressif)
    Espressif.show()
    sys.exit(app.exec_())


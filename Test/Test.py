from PyQt4 import QtCore, QtGui
import TestUI
import serial
import threading

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


class Test_Form(TestUI.Ui_Form, QtGui.QWidget):
    
    _printLog = QtCore.pyqtSignal(str)
    def __init__(self, SerialTool, parent=None):
        super(QtGui.QWidget, self).__init__(parent=parent) 
        self.setupUi(self)
        self.serialFoo(self)

    def serialFoo(self,SerialTool):
        QtCore.QObject.connect(self.StopButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.slot_stop)
        QtCore.QObject.connect(self.StartButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.slot_Start)
        self._printLog.connect(self.prinLog)
        
    def slot_Start(self):
        self.TextBroser.append("AAA")
        self._ser = serial.Serial(port="COM47",
                                              baudrate=115200,
                                            parity=serial.PARITY_NONE,stopbits=1,bytesize=8)  
        t1 = threading.Thread(target=self.cycTask,)
        t1.start() 
        
    def cycTask(self):
        while True:
            self._printLog.emit( str(self._ser.readline()))
        
    def prinLog(self,log):
        self.TextBroser.append(log)
    
    def slot_stop(self):
        self._ser.stop()
        
if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Test_Form(Form)
    #ui.setupUi(Form)
    ui.show()
    sys.exit(app.exec_())
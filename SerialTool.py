import SerialToolUI
import threading
import os
import time
import serial
import serial.tools.list_ports
from PyQt4 import QtCore, QtGui
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

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
    
    
plist = []


def SerialTool(plist):
    if len(plist) <= 0:
        print ("The Serial port can't find!")
    else:
        for i in plist:
            print str(i)[0:int(str(i).find(" "))]
        plist_0 =list(plist[0])
        serialName = plist_0[0]
        serialFd = serial.Serial("COM47",74880,timeout = 60)
        serialFd.bytesize = 8
        serialFd.parity = serial.PARITY_NONE  # PARITY_EVEN 偶 PARITY_ODD 奇
        serialFd.stopbits = 1
        
        print ("check which port was really used >",serialFd.name)
        print serialFd.name
        while True:
            if timeFlag == 1:
                print time.asctime( time.localtime(time.time()) ) + serialFd.readline()
            elif timeFlag == 0:
                print time.asctime( time.localtime(time.time()) ) + serialFd.readline()
                

class UI_Test(SerialToolUI.Ui_Form,QtGui.QWidget):
    
    
    _printLog = QtCore.pyqtSignal(str)
    _OpenCloseFlag = 0
    _timeFlag = 0
    
    
    def __init__(self, SerialTool, parent=None):
        super(QtGui.QWidget, self).__init__(parent=parent)
        #self._SignalStart.connect(self.ok_button)
        self.setupUi(self)
        self.serialFoo(self)
        self.cominfoget(self)
    
    def cominfoget(self, SerialTool):
        plist = list(serial.tools.list_ports.comports())
        if len(plist) <= 0:
            print ("The Serial port can't find!")
        else:
            for i in plist:
                print str(i)[0:int(str(i).find(" "))]
                self.comchoose.addItem(str(i)[0:int(str(i).find(" "))])
    
        
    def serialFoo(self,SerialTool):
        self.portoperate.clicked.connect(self.portoperateFoo)
        self.Time.clicked.connect(self.timeLog)
        #self._printLog.connect(self.printLog)
    
    def timeLog(self):
        if _timeFlag == 0:
            _timeFlag==1;
        else:
            _timeFlag = 0
            
        
    def portoperateFoo(self):
        if self._OpenCloseFlag == 0:
            self._OpenCloseFlag = 1
            
            if str(self.checkchoose.currentText()).find('custom') >= 0:             
                baudRate = int(self.baudEdit.text())
            else:
                baudRate = str(self.baudratelchoose.currentText())
                #self.baudEdit.setText(baud_rate)
                
            
            comPort = str(self.comchoose.currentText())
            baudRate =  int(self.baudratelchoose.currentText())  
            print "================="
            comPort = "COM47"
            print baudRate
            self._ser = serial.Serial(port=comPort,
                                      baudrate=baudRate,
                                            parity=serial.PARITY_NONE,stopbits=1,bytesize=8) 
            #self._ser.open()
            #self.serialFd = serial.Serial(port=comPort,baudrate=baundRate,timeout = 60)
            
            '''
            if(str(self.checkchoose.currentText()) == '无'):
                erialFd.parity = serial.PARITY_NONE
            elif(str(self.checkchoose.currentText()) == '奇校验'):
                serialFd.parity = serial.PARITY_ODD
            elif(str(self.checkchoose.currentText()) == '偶校验'):
                serialFd.parity = serial.PARITY_EVEN
            serialFd.stopbits = int(self.stopChoose.currentText())
            '''
            t1 = threading.Thread(target=self.cycTask)
            t1.start()    
        elif self._OpenCloseFlag == 1:
            self._OpenCloseFlag == 0
        
        print str(self._OpenCloseFlag) + "----"

    def printLog(self, log):
            print log
            
    def cycTask(self):
            while True:
                if self._OpenCloseFlag == 0:
                    print "Close"
                elif self._OpenCloseFlag == 1:
                    print "Open"
                #print str(time.asctime( time.localtime(time.time()) ) + self._ser.readline())
                #self._printLog.emit(time.asctime( time.localtime(time.time()) ) + self._ser.readline())
                time.sleep(1)            
            
            
    

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SerialTool = QtGui.QWidget()
    SerialToolui = UI_Test(SerialTool)
    SerialToolui.setupUi(SerialTool)
    #SerialTool.show()
    SerialToolui.show()
    sys.exit(app.exec_())
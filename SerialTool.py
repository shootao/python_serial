import SerialToolUI
import threading
import os
import sys
import time
import serial
import serial.tools.list_ports
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

'''
 from PyQt4.QtGui import *
 from PyQt4.QtCore import *
        palette1 = QtGui.QPalette(self)
        palette1.setColor(self.backgroundRole(), QColor(192,253,123))   # …Ë÷√±≥æ∞—’…´
        # palette1.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap('../../../Document/images/17_big.jpg')))   # …Ë÷√±≥æ∞Õº∆¨
        self.setPalette(palette1)       
'''



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
        serialFd.parity = serial.PARITY_NONE  # PARITY_EVEN ≈º PARITY_ODD ∆Ê
        serialFd.stopbits = 1
        
        print ("check which port was really used >",serialFd.name)
        print serialFd.name
        while True:
            if timeFlag == 1:
                print time.asctime( time.localtime(time.time()) ) + serialFd.readline()
            elif timeFlag == 0:
                print time.asctime( time.localtime(time.time()) ) + serialFd.readline()
                
class UI_Test(SerialToolUI.Ui_Espressif,QtGui.QWidget):
    
    _printLog = QtCore.pyqtSignal(str)
    _OpenCloseFlag = 0
    _timeFlag = 0
    _sendNewLine = 0
    
    def __init__(self, SerialTool, parent=None):
        super(QtGui.QWidget, self).__init__(parent=parent)
        #self._SignalStart.connect(self.ok_button)
        self.setupUi(self)
        self.serialFoo(self)
        self.cominfoget(self)
        self.portoperate.setStyleSheet("background-color: green")
        
    
    def cominfoget(self, SerialTool):
        plist = list(serial.tools.list_ports.comports())
        if len(plist) <= 0:
            print ("The Serial port can't find!")
        else:
            for i in plist:
                print i[0]#str(i)[0:int(str(i).find(" "))]
                self.comchoose.addItem(_fromUtf8(i[0]))
                #self.comchoose.addItem(str(i)[0:int(str(i).find(" "))])
    
        
    def serialFoo(self,SerialTool):
        self.portoperate.clicked.connect(self.portoperateFoo)
        #Sself.Time.clicked.connect(self.timeLog)
        self._printLog.connect(self.printLog)
        self.Time.stateChanged.connect(self.changeTimeStatus)
        self.SendNewLine.stateChanged.connect(self.addNewSendLine)
        self.saveInfo.clicked.connect(self.saveInfofoo)
        self.clearInfo.clicked.connect(self.ClearInfoFoo)
        self.inFoSend.clicked.connect(self.inFoSendFoo)
        self.InfoClear.clicked.connect(self.InfoClearFoo)
    
    
    def InfoClearFoo(self):
        self.lineEditCommand.clear()
    
    def ClearInfoFoo(self):
        self.InfoBrower.clear()
    
    def saveInfofoo(self, SerialTool):
        filename = QtGui.QFileDialog.getSaveFileName(None, 'Save file', './')
        try:
            with open(filename, 'w') as fd:
                fd.write(str(self.InfoBrower.toPlainText()))
        except:
            pass   
        
    def portoperateFoo(self):
        print self._OpenCloseFlag
        if self._OpenCloseFlag == 1:
            self.portoperate.setStyleSheet("background-color: green")
            self.portoperate.setText('Close')
            self._OpenCloseFlag = 0
            #self._ser.close()
            return
        elif self._OpenCloseFlag == 0:
            self._OpenCloseFlag = 1
            self.portoperate.setStyleSheet("background-color: red")
            self.portoperate.setText('Open')
            
            comPort = str(self.comchoose.currentText())
            baudRate = int(self.baudratelchoose.currentText())        
         
            try:
                self._ser = serial.Serial(port=comPort,
                                        baudrate=baudRate,
                                        parity=serial.PARITY_NONE,stopbits=1,bytesize=8)

            except:
                #self.printLog('open serial fail...')
                #msg_box = QMessageBox(QMessageBox.Warning, "Alert", "Please configure the baseline!")
                #msg_box.show()          
                QMessageBox.information(self,                         # π”√infomation–≈œ¢øÚ    
                                        "Waring",    
                            "The serial port is occupied")                
                return  

            t1 = threading.Thread(target=self.cycTask,)
            t1.start()  
        
            
            print self._OpenCloseFlag

    def cycTask(self):
        while True:
            #print str(time.asctime( time.localtime(time.time()) ) + self._ser.readline())
            self._printLog.emit( self._ser.readline())

    def printLog(self, log):
        if self._timeFlag == 1:
            print  time.asctime( time.localtime(time.time()) )+"[LOG]"+log
            if log != "":
                self.InfoBrower.append(time.asctime( time.localtime(time.time()) )+" => "+log)
        elif self._timeFlag == 0:
            self.InfoBrower.append(log)

    def changeTimeStatus(self, state):
        if state == QtCore.Qt.Checked:
            self._timeFlag = 1
        else:
            self._timeFlag = 0
    
    def addNewSendLine(self, state):
        if state == QtCore.Qt.Checked:
            self._sendNewLine = 1
            print ('QtGui.QCheckBox')
        else:
            self._sendNewLine = 0
            
    def inFoSendFoo(self):
        print self.lineEditCommand.text()
        if self._sendNewLine==1:
            self._ser.write(str(self.lineEditCommand.text())+"\r\n")
        else:
            self._ser.write(str(self.lineEditCommand.text()))
            
 

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    SerialTool = QtGui.QWidget()
    SerialToolui = UI_Test(SerialTool)
    #SerialToolui.setupUi(SerialTool)
    #SerialTool.show()
    SerialToolui.show()
    sys.exit(app.exec_())
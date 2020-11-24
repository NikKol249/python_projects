import sys
#from PyQt5.QtWidgets import QApplication, QWidget
#from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtWidgets, QtCore, QtGui
import serial
import commands
import time
#import threading

response = list()
text = list()

class MyThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None):
        QtCore.QThread.__init__(self, parent)
    def run(self):
        for i in range(1, 21):
            self.sleep(10)
            self.mysignal.emit('i= %s' % i)

class Cab_window(QtWidgets.QWidget):
    from PyQt5 import QtCore

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        #super().__init__()
        #self.initUI()
        
    #def initUI(self):

            
        '''
        def program(aelf):

            ser = list()
            COM_PORT =  [comboboxPort.currentText()]
            Year = list(SpinBoxYear.cleanText())
            number = list(Number.text())
            ser.append(str(type.get(comboboxType.currentText())))
            ser = ser + Year
            ser = ser + number
            ser.append(str(typecable.get(comboboxTypeCable.currentText())))
            '''
            
        self.comboboxPort = QtWidgets.QComboBox(self)
        self.comboboxPort.resize(260,30)
        self.comboboxPort.move(20,20)
        #self.comboboxPort.setStyleSheet('QComboBox{background-color: #FFFFFF; border: [10 || solid || #3B423B]; font-size: 10pt; color: #212121}; QComboBox:editable{background-color: #FFFFFF} ')
        self.comboboxPort.setStyleSheet('QComboBox{background-color: #3B3B3B; font-size: 10pt; color: #FFFFFF; border: 1 solid #262B26; selection-background-color: #262B26;} QComboBox QAbstractItemView { border: 1 solid #262B26; selection-background-color: #262B26; font-size: 12 pt #FFFFFF background-color: #FFFFFF }')
        self.comboboxPort.addItems(commands.serial_ports())

        self.type = {'KR0':0, 'KR1':1, 'KR2':2, 'KR3':3, 'PM3':4,}
        self.comboboxType = QtWidgets.QComboBox(self)
        self.comboboxType.resize(50,30)
        self.comboboxType.move(20,70)
        self.comboboxType.setStyleSheet('QComboBox{background-color: #3B3B3B; font-size: 10pt; color: #FFFFFF; border: 1 solid #262B26; selection-background-color: #262B26;} QComboBox::QAbstractItemView { border: 1 solid #262B26; selection-background-color: #262B26; font-size: 12 pt #FFFFFF background-color: #FFFFFF }')
        self.comboboxType.addItems(self.type.keys())

        
        self.SpinBoxYear = QtWidgets.QDateEdit(self)
        self.SpinBoxYear.resize(60,30)
        self.SpinBoxYear.move(80,70)
        self.SpinBoxYear.setDisplayFormat('yyyy')
        self.SpinBoxYear.setStyleSheet('QDateEdit{background-color: #3B3B3B; font-size: 10pt; color: #FFFFFF; border: 1 solid #262B26; selection-background-color: #262B26;} QDateEdit::QAbstractItemView { border: 1 solid #3B423B; selection-background-color: #262B26; font-size: 12 pt #FFFFFF background-color: #FFFFFF }')
        
        self.Number = QtWidgets.QLineEdit(self)
        self.Number.resize(70,30)
        self.Number.move(150,70)
        self.Number.setMaxLength(4)
        self.Number.setStyleSheet('background-color: #3B3B3B; font-size: 10pt; color: #FFFFFF; border: 1 solid #262B26; selection-background-color: #262B26;')
        
        self.typecable = {'5':1,'7':2,'10':3}
        self.comboboxTypeCable = QtWidgets.QComboBox(self)
        self.comboboxTypeCable.resize(50,30)
        self.comboboxTypeCable.move(230,70)
        self.comboboxTypeCable.setStyleSheet('QComboBox{background-color: #3B3B3B; font-size: 10pt; color: #FFFFFF; border: 1 solid #262B26; selection-background-color: #262B26;} QComboBox QAbstractItemView { border: 1 solid #3B423B; selection-background-color: #262B26; font-size: 12 pt #FFFFFF background-color: #FFFFFF }')
        self.comboboxTypeCable.addItems(self.typecable.keys())

        self.LineEdit = QtWidgets.QTextEdit(self)
        self.LineEdit.resize(260,30)
        self.LineEdit.move(20,120)
        self.LineEdit.setStyleSheet('background-color: #3B3B3B; font-size: 10pt; color: #FFFFFF; border:  solid #262B26; selection-background-color: #262B26;')
        self.LineEdit.setReadOnly(True)
        #LineEdit.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

        self.mythread = MyThread()

        

        self.buttonProgram = QtWidgets.QPushButton('Program', self)
        self.buttonProgram.setFixedSize(100,40)
        self.buttonProgram.move(180,170)
        #self.buttonProgram.keyPressEvent('e')
        self.buttonProgram.setStyleSheet(' QPushButton {background-color: #3B3B3B; font-size: 10pt; color: #FFFFFF; border: 1 solid #262B26; selection-background-color: #262B26;} QPushButton:pressed{background-color: #2F2F2F;font-size: 10pt; color: #E1FFF1;}')
        self.buttonProgram.setShortcut('return')
        self.buttonProgram.clicked.connect(self.program)
        #self.mythread.started.connect(self.on_started)
        #self.mythread.finished.connect(self.on_finished)
        #self.buttonProgram.clicked.connect(print(SpinBoxYear.text()))
        #self.mythread.mysignal.connect(self.on_change, QtCore.Qt.QueuedConnection)

    



        self.progressbar = QtWidgets.QProgressBar(self)
        self.progressbar.resize(140,20)
        self.progressbar.move(20,170)
        self.progressbar.setStyleSheet('background-color: #3B3B3B; border: 1 solid #262B26; selection-background-color: #262B26;')
        self.progressbar.setTextVisible(False)

        self.TextEdit = QtWidgets.QTextEdit(self)
        self.TextEdit.resize(140,60)
        self.TextEdit.move(20,200)
        self.TextEdit.setStyleSheet('background-color: #3B3B3B; font-size: 10pt; color: #FFFFFF;; border: 1 solid #262B26; selection-background-color: #262B26;')
        self.TextEdit.setReadOnly(True)

        self.buttonExit = QtWidgets.QPushButton('Exit', self)
        self.buttonExit.setFixedSize(100,40)
        self.buttonExit.move(180,220)
        self.buttonExit.setStyleSheet('QPushButton {background-color: #3B3B3B; font-size: 10pt; color: #FFFFFF; border: 1 solid #262B26; selection-background-color: #262B26;} QPushButton:pressed{background-color: #2F2F2F; font-size: 10pt; color: #E1FFF1;}')
        self.buttonExit.setShortcut('esc')
        self.buttonExit.clicked.connect(QtCore.QCoreApplication.instance().quit)

        
        #-------------------------------------------------------    
    def checkPort(self, COM):
        try:
            port = serial.Serial(COM, 921600)
            if port.isOpen() == True:
                port.write([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])  
                return 0
        except:
            return 1
        #----------------------------------------------------

    #def checkID():

        #----------------------------------------------------
       
    def sendData(self, COM, data_):
        try:
            port = serial.Serial(COM, 921600)
            global text
            text = data_
            data = list()
            for i in range(len(text)):
                a = hex(ord(text[i]))
                b = int(a, base=16)
                data.append(b)           
            port.write(data)
            global response
            r = port.bytesize
            response = port.read(r)
            return 1
        except:
            return 0

        #--------------------------------------------------------

    def feedback(self):
        #print(list(response))
        data = list()
        for i in range(len(text)):
            a = hex(ord(text[i]))
            b = int(a, base=16)
            data.append(b)
        #print(data)
        
        if list(response) == data:
            return 1
        else:
            return 0

        #--------------------------------------------------------

    def program(self):
        b = list()
        a =  [self.comboboxPort.currentText()]
        Year = list(self.SpinBoxYear.text())
        number = list(self.Number.text())
        b.append(str(self.type.get(self.comboboxType.currentText())))
        b.append(Year[2])
        b.append(Year[3])
        b = b + number
        b.append(str(self.typecable.get(self.comboboxTypeCable.currentText())))
        full_data = ' '.join(b)
        self.LineEdit.setText(full_data)
        self.LineEdit.setAlignment(QtCore.Qt.AlignCenter | QtCore.Qt.AlignCenter)

        try:
            for i in range(0,33):
                time.sleep(0.01)   
                self.progressbar.setValue(i)
            if self.checkPort(a[0]) == 1:
                self.TextEdit.append('Check port: <font color = green><\font> OK!')

                #if readID() == 1:
                #    for i in range(25,50):
                #        time.sleep(0.01)   
                #        progressbar.setValue(i)
                #    TextEdit.append('Read ID: <font color = green><\font> OK!')

                for i in range(33,66):

                    time.sleep(0.01)   
                    self.progressbar.setValue(i) 
                if self.sendData(a[0],b) == 1:
                    self.TextEdit.append('Send data:  <font color = green><\font> OK!')

                    for i in range(66,101):
                        time.sleep(0.01)   
                        self.progressbar.setValue(i)
                    if self.feedback() == 1:
                        self.TextEdit.append('FeedBack:  <font color = green><\font> OK!')
                        self.TextEdit.append('<font color = green><\font> Done!')

                    else:
                        self.progressbar.setValue(0)
                        self.TextEdit.append('Feedback:  <font color = red><\font> Error!')
                        self.TextEdit.append('<font color = red><\font> Error!')

                else:
                    self.progressbar.setValue(0)
                    self.TextEdit.append('Send data:  <font color = red><\font> Error!')
                    self.TextEdit.append('<font color = red><\font> Error!')
            
                #else:
                #    self.TextEdit.append('Read ID: <font color = red><\font> Error!')\
                #    self.TextEdit.append('<font color = red><\font> Error!')

            else:
                self.progressbar.setValue(0)
                self.TextEdit.append('Check port: <font color = red><\font> Error!')
                self.TextEdit.append('<font color = red><\font> Error!')

        except:
            self.progressbar.setValue(0)
            self.TextEdit.append('<font color = red><\font> Uncknow Error!')
        
        #----------------------------------------------

    def on_clicked(self):
        self.buttonProgram.setDisabled(True)
        self.mythread.start()
    
    def on_started(self):
        self.TextEdit.setText('Запуск')
    
    def on_finished(self):
        self.buttonProgram.setDisabled(False)
    
    def on_change(self, s):
        self.TextEdit.append(s)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ex = Cab_window()
    ex.setFixedSize(300, 280)
    ex.setWindowTitle('Cabeleble_BETA')
    ex.setStyleSheet('background-color: #2B2A29; border: 2 solid #262B26')
    ex.setWindowIcon(QtGui.QIcon('image.png'))
    ex.show()
    sys.exit(app.exec_())
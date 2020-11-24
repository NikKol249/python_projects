from PyQt5 import QtWidgets, QtCore, QtGui
import sys
import commands

def unf():
    a = [combobox.currentText()]
    b = LineEdit.text()    
    #commands.program(a[0],b)
    if (commands.program(a[0],b)) == 'Done':
        text = 'Done'
    else:
        text = 'Error'
    label = QtWidgets.QLabel(text, flags=QtCore.Qt.ToolTip)
    label.resize(100,100)
    label.show()
    
app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowFlags(QtCore.Qt.Widget)
window.setFixedSize(260,200)
window.setWindowIcon(QtGui.QIcon('image.png'))
window.setStyleSheet('background-color: #EDEDED')
window.setWindowTitle('Cabeleble')

LineEdit = QtWidgets.QLineEdit(window)
LineEdit.resize(220,30)
LineEdit.setMaxLength(8)
LineEdit.move(20,80)
LineEdit.setStyleSheet('background-color: #FFFFFF;')

combobox = QtWidgets.QComboBox(window)
combobox.resize(220,30)
combobox.move(20,20)
combobox.setStyleSheet('QComboBox{background-color: #FFFFFF;} QComboBox:pressed{background-color: #FAF3D2;}')
combobox.addItems(commands.serial_ports())

buttonExit = QtWidgets.QPushButton('Exit', window)
buttonExit.setFixedSize(100,40)
buttonExit.move(140,140)
buttonExit.setStyleSheet('QPushButton {background-color: #E1E1E1;} QPushButton:pressed{background-color: #FAF3D2;}')
buttonExit.clicked.connect(window.close)

buttonProgram = QtWidgets.QPushButton('Program', window)
buttonProgram.setFixedSize(100,40)
buttonProgram.move(20,140)
buttonProgram.setStyleSheet('QPushButton {background-color: #E1E1E1;} QPushButton:pressed{background-color: #FAF3D2;}')
buttonProgram.clicked.connect(unf)

window.show()
sys.exit(app.exec_())

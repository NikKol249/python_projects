import sys
import glob
import serial
import main
#COM ='COM3'
#data ='KR220041'

def readd(COM):
    port = serial.Serial(COM, 921600)
    text = port.read(28)
    return(text)

def program(COM, data_):
    
    port = serial.Serial(COM, 921600)

    #port.write([0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00])
    while port.isOpen:
        try:
            text = list(data_)
            data = []
            
            for i in range(len(text)):
                a = hex(ord(text[i]))
                b = int(a, base=16)
                data.append(b)
                    
            port.write(data)
            response = list(port.read(8))
        
            if response == data:
                text1 = '<font color = green><\font> Done'
            else:
                text1 = '<font color = red><\font> Error'
            return(text1)
        except:
            return('<font color = red><\font> Error')
    
    
    


def serial_ports():

    if sys.platform.startswith('win'):
        #ports = ['COM%s' % (i + 1) for i in range(256)]
        ports = ['COM%s' % (i + 1) for i in range(256)]
    #elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        #ports = glob.glob('/dev/tty[A-Za-z]*')
    #elif sys.platform.startswith('darwin'):
        #ports = glob.glob('/dev/tty.*')
    
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

import serial # if you have not already done so
from time import sleep

with open("/path/to/file/mytext.txt") as file:  #change path accordingly
        textStr = file.read()
with open("/path/to/file/subcount.txt") as file:
        subStr = file.read()

ser = serial.Serial('/dev/ttyUSB0')
sleep(3)
ser.baudrate = 9600
ser.write(b'1\r\n')
txt = ' ' + textStr + ' Current subs: ' + subStr + '   ' + '\r\n'
ser.write(str.encode(txt))
ser.close()

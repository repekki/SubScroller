import serial # if you have not already done so
from time import sleep

# testing to see that data can be sent through the serial port
ser = serial.Serial('/dev/ttyUSB0')
sleep(3)
ser.baudrate = 9600
ser.write(b'1\r\n')
ser.write(b' example ')y

""""Testing te tilt pan functionality from python (adjust the serial port-name) """"

import time
import serial


ser = serial.Serial()

ser.baudrate = 115200
ser.port = 'COM2'
ser.open()

print("send @")
ser.write(bytearray([64]))
time.sleep(1)

print("pos 10")
ser.write(bytearray([48,10]))
time.sleep(1)

print("pos 150")
ser.write(bytearray([48,150]))
time.sleep(1)

print("pos 10")
ser.write(bytearray([48,10]))
time.sleep(1)

print("pos 150")
ser.write(bytearray([48,150]))
time.sleep(1)




for pos in range (10,150,5):
    ser.write(bytearray([49,pos]))
    time.sleep(0.1)



"""
for pos in range(0,360,10):
    ser.write(bytearray([48,150*(1+math.cos(3.14*pos/180))]))
    ser.write(bytearray([49,150*(1+math.sin(3.14*pos/180))]))
    time.sleep(0.1)
"""

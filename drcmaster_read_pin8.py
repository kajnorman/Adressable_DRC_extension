from time import sleep
import serial

def readresponse():
        b = bytearray(b"                   ");
        ser.readinto(b)  #beware of timing issues here
        print(b)

#setup serial connection
ser = serial.Serial('/dev/ttyACM0',115200,timeout=0.5)  # open serial port
print(ser.name)         # check which port was really used
sleep(3)
#when the serial connection is initialized the usb-power is "flicked"
#causing the arduino to boot and thereby iddentify itself
readresponse()


ser.write(':'.encode('ascii'))
ser.write('y'.encode('ascii'))
ser.write('i'.encode('ascii'))  #set pin 8 as input
ser.write(b"\x08")

print("Blinking pin8 status  ctrl-c to terminate  :-) ")
while True:
	ser.write(':'.encode('ascii'))
	ser.write('y'.encode('ascii'))
	ser.write('r'.encode('ascii')) #reading the status of pin 8
	ser.write(b"\x08")
	readresponse()



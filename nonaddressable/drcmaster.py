from time import sleep
import serial

def readresponse():
        b = bytearray(b"                   ");
        ser.readinto(b) #when the serial connection is initialized the usb-power is "flicked"
        print(b)

#setup serial connection
ser = serial.Serial('/dev/ttyACM0',115200,timeout=0.5)  # open serial port
print(ser.name)         # check which port was really used
sleep(3)
#when the serial connection is initialized the usb-power is "flicked"
#causing the arduino to boot and thereby iddentify itself
readresponse()


ser.write(b'@')
readresponse()


ser.write(b"r\x07")   #reading the status of pin 7
print("pin7 status")
readresponse()

ser.write(b"o\x07")     #set pin 7 as output

print("Blinking pin7 status  ctrl-c to terminate  :-) ")
while True:
        ser.write(b"1\x07")     #set pin 7 high
        sleep(0.2)
        ser.write(b"0\x07")   #set pin 7 low
        sleep(0.2)



from time import sleep
import serial

// this driveunit is based on a specific  Robocar
// this is based on Gordons DRC-protocol running on Arduino


def readresponse():
        b = bytearray(b"                   ");
        ser.readinto(b) #when the serial connection is initialized the usb-power is "flicked"
        print(b)

#setup serial connection
#ser = serial.Serial('/dev/ttyACM0',115200,timeout=0.5)  # open serial port on usb from Raspberry
ser = serial.Serial('COM9',115200,timeout=0.5)  # open serial port  from wind PC
print(ser.name)         # check which port was really used
sleep(3)
#when the serial connection is initialized the usb-power is "flicked"
#causing the arduino to boot and thereby iddentify itself
readresponse()
// shows DRC_versiion

ser.write(b'@')
readresponse()
//Respose to a ping


//initializing pins on an arduino
ser.write(b"o\x05")     #set pin 5,6,9,10 as output
ser.write(b"o\x06")     #5 and 6 are on the H-bridge connected to the left side of the Car
ser.write(b"o\x09")     #9 and 10 are on the H-bridge connected to the right side of the Car
ser.write(b"o\x0A")



def Right_Forwards():
        ser.write(b"1\x0A")  # set pin 5 high
        ser.write(b"0\x09")

def Right_Forwards_halfspeed():
        ser.write(b"v\x0A\x7F")  # set pin x0a to a value of 0x7F (half speed)
        ser.write(b"0\x09")


def Left_Forwards():
        ser.write(b"1\x05")  # set pin 5 high
        ser.write(b"0\x06")

def Right_Stop():
        ser.write(b"0\x0A")  # set pin 5 high
        ser.write(b"0\x09")

def Left_Stop():
        ser.write(b"0\x05")  # set pin 5 high
        ser.write(b"0\x06")

def Stop():
        Left_Stop()
        Right_Stop()

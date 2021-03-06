/*
   PanTiltDRC
   Arduino code to implement control of pan and tilt  using
        Two RC-servos
        One Arduino
        And a modified version of DRC - The Drogon Remote Control.
   Allow another device talking to us over the serial port to control the
  IO pins.
   DRC originally Copyright (c) 2012 Gordon Henderson
   Full details at:
   http://projects.drogon.net/drogon-remote-control/drc-protocol-arduino/
   Commands:
   @: 0x40 Ping          Send back #: 0x23
   0: 0x30 0xNN  Set servo position of servo on pin 2 to NN (degrees)
   0: 0x31 0xNN  Set servo position of servo on pin 3 to NN (degrees)
*************************************************************************
********
   This file is part of drcAduino:
   Drogon Remote Control for Arduino
   http://projects.drogon.net/drogon-remote-control/
   drcAduino is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.
   drcAduino is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.
   You should have received a copy of the GNU General Public License
   along with drcAduino.  If not, see <http://www.gnu.org/licenses/>.
*************************************************************************
********
*/
// Serial commands
#define CMD_PING        '@'
#define CMD_SERVO_PIN_2       '0'
#define CMD_SERVO_PIN_3       '1'
#include <Servo.h>

Servo pan,tilt;  // create servo object to control a servo
// twelve servo objects can be created on most boards



void setup ()
{

  Serial.begin (115200) ;
  Serial.println ("DRC Arduino 1.0") ;
  pan.attach(2);  // attaches the servo on pin 2 to the servo object
  tilt.attach(3);  // attaches the servo on pin 2 to the servo object
}

int myGetchar ()
{
  int x ;
  while ((x = Serial.read ()) == -1)
    ;
  return x ;
}

void loop ()
{
  unsigned int pin ;
  unsigned int aVal, dVal ;
  int pos ;
  for (;;)
  {
    if (Serial.available () > 0)
    {
      switch (myGetchar ())
      {
        case CMD_PING:
          Serial.write (CMD_PING) ;
          continue ;


        case CMD_SERVO_PIN_2: //pan
          pos  = myGetchar () ;
          if ((pos >= 0) && (pos <= 180))
            pan.write(pos);
          continue ;


        case CMD_SERVO_PIN_3:  //tilt
          pos  = myGetchar () ;
          if ((pos >= 0) && (pos <= 180))
            tilt.write(pos);
          continue ;



      }
    }
  }
}

#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks.messaging import BluetoothMailboxServer, TextMailbox


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()

#server = BluetoothMailboxServer()

#server.wait_for_connection(2)

#start = TextMailbox('start', server)

#while(button.CENTER not in buttons.pressed()):
#    pass

while True:
    if Button.CENTER in ev3.buttons.pressed():
        break
    else:
        pass

#start.send('START')

wait(5000)

# Write your program here.
ev3.speaker.beep()

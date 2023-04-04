#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
leftmotor = Motor(Port.B)
rightmotor = Motor(Port.C)
drivebase = DriveBase(leftmotor, rightmotor,
                       wheel_diameter=56, axle_track=112)
# Write your program here.
# leftmotor.run_angle(360, 360, then=Stop.HOLD, wait=True)
drivebase.straight(1000)
ev3.speaker.beep()
while True:
    drivebase.drive(360,0)

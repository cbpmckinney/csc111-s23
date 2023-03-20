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

gyro = GyroSensor(Port.S1)
leftmotor = Motor(Port.C)
rightmotor = Motor(Port.B)
robot = DriveBase(leftmotor, rightmotor, wheel_diameter=55.5, axle_track=104)

targetheading = 0
kp = 1

while True:
    error = gyro.angle() - targetheading
    robot.drive(100, kp*error)




# Write your program here.
ev3.speaker.beep()

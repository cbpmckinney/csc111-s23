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
mywatch = StopWatch()

gyro = GyroSensor(Port.S1)
leftmotor = Motor(Port.C)
rightmotor = Motor(Port.B)
robot = DriveBase(leftmotor, rightmotor, wheel_diameter=55.5, axle_track=104)

targetheading = 0
kp = 2
kd = 121
ki = 1

mywatch.reset()
mywatch.resume()
currenttime = 0
oldtime = 0
currenterror = 0
olderror = 0
while True:
    currenttime = mywatch.time()
    currenterror = gyro.angle() - targetheading
    try:
        rateoferror = (currenterror - olderror)/(currenttime - oldtime)
        print(rateoferror)
    except:
        rateoferror = 0
        print("exception!")

    robot.drive(100, kp*currenterror + kd*rateoferror)
    oldtime = currenttime
    olderror = currenterror
    wait(1)




# Write your program here.
ev3.speaker.beep()

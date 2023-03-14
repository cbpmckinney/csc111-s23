#!/usr/bin/env pybricks-micropython


from ev3dev2.motor import (
    MoveSteering, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C)
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep


# Start robot moving forward


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()
motor_pair = MoveSteering(OUTPUT_B, OUTPUT_C)
medium_motor = MediumMotor(OUTPUT_A)
ultrasonic_sensor = UltrasonicSensor()

# Write your program here.
ev3.speaker.beep()
motor_pair.on(steering=0, speed=10)

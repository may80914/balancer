#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# Write your program here
brick.sound.beep()

gyro = GyroSensor(Port.S3)
motor1 = Motor(Port.B)
motor2 = Motor(Port.C)
robot = DriveBase(motor1, motor2, 56, 50)

gyro.reset_angle(0)
#Must start robot in upright balanced position

while True:
 print(gyro.angle())
 robot.drive(5*gyro.angle(),0)

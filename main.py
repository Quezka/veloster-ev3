#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Color, Button
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
import time
ev3 = EV3Brick()
msx = Motor(Port.A)
msd = Motor(Port.D)
radar = InfraredSensor(Port.S4)

robot = DriveBase(msx, msd, 43, 152)

startUpFase = False
runningFase = False
def checkDistanceToWall(InfraredSensor):
    distance = InfraredSensor.distance()
    if distance == 20 or distance < 20:
        return distance, "Distanza < o = 20%"


while True:
    time.sleep(1)
    checkDistanceToWall(radar)

while startUpFase:
    proceed = False

robot.straight(100)


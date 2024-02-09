#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Color, Button
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

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
        return "Distanza <= 20%"
    else:
        return "Distanza > 20%"


while True:
    ev3.wait(100)
    ev3.screen.clear()
    ev3.scrren.print(checkDistanceToWall(radar))

while startUpFase:
    proceed = False

robot.straight(100)


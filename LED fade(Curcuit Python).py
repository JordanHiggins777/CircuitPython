# Assignment 1 Led Fade

import board
from analogio import AnalogOut
import time
import neopixel

yeet = 0  #Power
yote = 1  #Bool
pin = 13  #Pin

analog_out = AnalogOut(board.A0)


while True:
    if(yote==1):   # fade in
        yeet +=10

    if(yote==0):
        yeet -=10     # fade out

    if(yeet >= 65000):
        yote= 0
    if(yeet <=0):      # range of light
        yote=1


    analog_out.value = yeet
#Assignment 5 Sonar and NeoPixel

import math
import time
import board
import neopixel
import adafruit_hcsr04

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)  # establishes the NeoPixel

sonar = adafruit_hcsr04.HCSR04(board.D3, board.D2)  # establishes the sonar

r = 0   #establishes red
g = 0   #establishes green
b = 0   #establishes blue

while True:


    print(int(g))
    if r < 0:
        r = 0
    if r > 255:     # makes led not go past 255 or below 0
        r = 255


    if b < 0:
        b = 0
    if b > 255:     # makes led not go past 255 or below 0
        b = 255

    if g < 0:
        g = 0
    if g > 255:     # makes led not go past 255 or below 0
        g = 255



    dot.fill((int(r), int(g), int(b)))

    try:


        r =(-((sonar.distance)*8)+127)

        b =(((sonar.distance)*8)-127) # graphing equasions put into code

        g =-(abs(((sonar.distance)*8)-127))+100



    except RuntimeError:
        print("Retrying!")
        r = 0
        g = 0       # incase of a RuntimeError
        b = 0
        pass
    time.sleep(0.1)  #delay
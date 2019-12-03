#Assignment 2 Servo: Uses capacitive touch to control a servo

import touchio
import time
import board
import pulseio
from adafruit_motor import servo

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)

angle = 90

touch_A4 = touchio.TouchIn(board.A4)  # Not a touch pin on Trinket M0!
touch_A5 = touchio.TouchIn(board.A5)  # Not a touch pin on Trinket M0!

while True:
    if touch_A4.value:
        print("Touched A4!")
        angle += 1
    if touch_A5.value:
        print("Touched A5!")
        angle -= 1
    if angle>180:
        angle=180
    if angle<0:
        angle=0

    my_servo.angle = angle


import time
import board
from rgb import RGB   # import the RGB class from the rgb module


r1 = board.D3
g1 = board.D2
b1 = board.D1
r2 = board.D12
g2 = board.D11
b2 = board.D10

myRGB1 = RGB(r1,g1,b1)   # create a new RGB object, using pins 3, 4, and 5
myRGB2 = RGB(r2,g2,b2)   # create a new RGB object, using pins 8, 9, and 10

while True:
    myRGB1.red()          # Glow red
    myRGB2.yellow()        # Glow green
    time.sleep(1)
    myRGB1.yellow()         # Glow blue
    myRGB2.green()         # Glow... you get it...
    time.sleep(1)
    myRGB1.green()      # Did you know magenta isn't in the rainbow?
    myRGB2.cyan()       # Like you learned in first grade, red and green make... huh?
    time.sleep(1)
    myRGB1.cyan()      # Did you know magenta isn't in the rainbow?
    myRGB2.blue()       # Like you learned in first grade, red and green make... huh?
    time.sleep(1)

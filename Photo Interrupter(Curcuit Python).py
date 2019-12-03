#Assignment 4 Photo Interrupter

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import board
from lcd.lcd import CursorMode
import digitalio
import time

# Talk to the LCD at I2C address 0x3f.
# The number of rows and columns defaults to 4x20, so those
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

Pi = digitalio.DigitalInOut(board.D2)
Pi.direction= digitalio.Direction.INPUT
Pi.pull = digitalio.Pull.UP

buttonState = 0
piState = 1
number = 0

initial = 0  # Time in seconds since power on

while True:
    now = time.monotonic()
    if now - initial > 3.999999 :  # If 4 seconds elapses
        lcd.clear()
        lcd.print("# of interrupts  ")

        lcd.print(str(number))
        initial = now

    if piState and not Pi.value:
        number +=1
    piState = Pi.value
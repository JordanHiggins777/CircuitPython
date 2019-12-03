#Assignment 3 Lcd and buttons


from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import board
from lcd.lcd import CursorMode
import digitalio

# Talk to the LCD at I2C address 0x3f.
# The number of rows and columns defaults to 4x20, so those
# arguments could be omitted in this case.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

button = digitalio.DigitalInOut(board.D2)
button.direction= digitalio.Direction.INPUT #Defines Button
button.pull = digitalio.Pull.DOWN

switch = digitalio.DigitalInOut(board.D5)
switch.direction = digitalio.Direction.INPUT #Defines Switch
switch.pull = digitalio.Pull.DOWN



buttonState = 0
switchState = 1
number = 0

while True:

    if not buttonState and button.value:
        number += switchState
    buttonState = button.value
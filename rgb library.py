from time import sleep
from digitalio import DigitalInOut, Direction #pylint: disable-msg=import-error

class RGB:

    def __init__(self, rpin, gpin, bpin):
        self.rpin = DigitalInOut(rpin)
        self.rpin.direction = Direction.OUTPUT

        self.gpin = DigitalInOut(gpin)
        self.gpin.direction = Direction.OUTPUT

        self.bpin = DigitalInOut(bpin)
        self.bpin.direction = Direction.OUTPUT

    def red(self):
        self.rpin.value = False
        self.gpin.value = True
        self.bpin.value = True

    def yellow(self):
        self.rpin.value = False
        self.gpin.value = False
        self.bpin.value = True

    def green(self):
        self.rpin.value = True
        self.gpin.value = False
        self.bpin.value = True

    def cyan(self):
        self.rpin.value = True
        self.gpin.value = False
        self.bpin.value = False

    def blue(self):
        self.rpin.value = True
        self.gpin.value = True
        self.bpin.value = False

    def magenta(self):
        self.rpin.value = False
        self.gpin.value = True
        self.bpin.value = False

#     def off(self):
#         self.rpin.value = True
#         self.gpin.value = True
#         self.bpin.value = True
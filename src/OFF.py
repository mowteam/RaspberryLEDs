import board
import neopixel
import sys
from settings import neopixelObject

#initialize pixels
pixels = neopixelObject()

#turn LEDs off
pixels.fill((0, 0, 0))
pixels.show()

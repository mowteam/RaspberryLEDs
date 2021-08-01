import board
import neopixel
from settings import neopixelObject

#initialize pixels
pixels = neopixelObject()

i = input("Enter a color (as R, G, B): ")
color = tuple(int(x) for x in i.split(","))
pixels.fill(color)
pixels.show()
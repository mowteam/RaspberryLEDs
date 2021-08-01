import board
import neopixel
from settings import num_pixels, pixels

i = input("Enter a color (as R, G, B): ")
color = tuple(int(x) for x in i.split(","))
pixels.fill(color)
pixels.show()
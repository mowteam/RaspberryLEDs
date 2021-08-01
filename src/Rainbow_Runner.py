import board
import neopixel
import random
import time
import numpy as np
from randomColorRainbow import random_color

#initialize pixels
pixel_pin = board.D18
num_pixels = 149
ORDER = neopixel.RGB 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER
)

def main():
	#set speed of runner in seconds
	speed = 0.05

	#set all pixels to the same random color
	pixels.fill(random_color())

	#run runner until user breaks loop
	while True:
		runner(speed)

def runner(speed):
	#choose random color
	color = random_color()

	#make the next light change to that color with time delay
	for i in range(num_pixels):
		pixels[i] = color
		pixels.show()
		time.sleep(speed)

main()
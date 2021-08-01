import board
import neopixel
import random
import time
from randomColorRainbow import random_color
from settings import num_pixels, pixels

def shoot():
	#make all one color
	background = random_color()
	pixels.fill(background)
	pixels.show()

	#initialize shooter
	length = 1 #length of bullet (LEDs)
	color = random_color()
	change_color(0, length, color)

	#shoot pixel
	for i in range(length, i):
		change_color(i, length, color) #move bullet
		change_color(i - length, length, background) #delete path of bullet
		pixels.show()
		time.sleep(0.05)

def change_color(index, length, color):
	for i in range(index, index + length):
		pixels[i] = color

while True:
	shoot()




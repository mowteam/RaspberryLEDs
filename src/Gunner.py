import board
import neopixel
import random
import time
from randomColorRainbow import random_color
from settings import num_pixels, pixels

def main():
	#make all red
	background = [255, 0, 0]
	pixels.fill(background)
	pixels.show()

	#initialize shooter
	color = random_color()
	pixels[0] = color

	#shoot pixel
	i = num_pixels
	while True:
		pixels[1] =  color
		pixels.show()
		time.sleep(0.05)

		#shoot pixel
		for i in range(2, i):
			pixels[i] = color
			pixels[i-1] = background
			pixels.show()
			time.sleep(0.05)

		#reduce range
		i--
main()





import neopixel
import time
from settings import num_pixels, pixels
from randomColorRainbow import random_color

def main():
	while True:
		for i in range(num_pixels):
                	pixels[i] = [255, 0, 0] #set red
		pixels.show()
		time.sleep(0.4) #pause
		pixels.fill([0, 0, 0]) #clear
		pixels.show()

main()

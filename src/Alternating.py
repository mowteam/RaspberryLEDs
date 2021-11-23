import neopixel
import numpy as np
from settings import num_pixels, pixels


def main():
	color1 = readColor()
	color2 = readColor()
	for i in range(num_pixels):
		if(i % 2 == 0):
			pixels[i] = color1
		else:
			pixels[i] = color2
	pixels.show()




def readColor():
	color = input("Enter R, G, B: ")
	return tuple(int(x) for x in color.split(","))
main()

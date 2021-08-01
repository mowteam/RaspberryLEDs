import board
import neopixel
import numpy as np
from settings import num_pixels, pixels

#turn all lights off
pixels.fill((0, 0, 0))
pixels.show()

#take input percentage
percentage = int(input("Enter the percent of lights on as an integer from 0 to 100: ")) / 100
i = input("Enter the primary color (as R, G, B): ")
color = tuple(int(x) for x in i.split(","))
i = input("Enter the secondary color (as R, G, B): ")
color2 = tuple(int(x) for x in i.split(","))

pixels.fill(color2)

for i in range(int(percentage * num_pixels)):
	r = np.random.randint(num_pixels)
	if(pixels[r] != color): #if not already on turn it on
		pixels[r] = color
	else:
		i -= 1

pixels.show()


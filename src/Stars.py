import board
import neopixel
import numpy as np

#initialize pixels
pixel_pin = board.D18
num_pixels = 149
ORDER = neopixel.RGB 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER
)

#turn all lights off
pixels.fill((0, 0, 0))
pixels.show()

#take input percentage
percentage = int(input("Enter the percent of lights on as an integer from 0 to 100: "))
i = input("Enter a color (as R, G, B): ")
color = tuple(int(x) for x in i.split(","))

for i in range(percentage):
	r = np.random.randint(num_pixels)
	if(pixels[r] != color): #if not already on turn it on
		pixels[r] = color
	else:
		i -= 1

pixels.show()
def main():
	import board
	import neopixel
	import random
	import time

	#initialize
	pixel_pin = board.D10
	num_pixels = 149
	ORDER = neopixel.GRB 
	pixels = neopixel.NeoPixel(
	    pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER
	)


	#set all pixels to the same random color
	pixels.fill(random_color())

	#run runner until user breaks loop
	while True:
		runner()


def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return [r, g, b]

def runner():
	#choose random color
	color = random_color()

	#make the next light change to that color with time delay
	for i in range(num_pixels):
		pixels[i] = color
		pixels.show()
		time.sleep(0.05)

main()
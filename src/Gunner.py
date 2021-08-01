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


def random_color():
	r = random.randint(0, 255)
	g = random.randint(0, 255)
	b = random.randint(0, 255)
	return [r, g, b]

main()




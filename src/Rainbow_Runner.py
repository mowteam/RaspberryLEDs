import board
import neopixel
import random
import time
import numpy as np

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


def random_color():
	arr = np.array([0, 1, 2]) #array to pick the colors from
	num = random.choice(arr) #which color is full on
	
	return setColors(num)

def createChoiceArray(num):
	arr = np.array(np.zeros(2))
	j = 0
	for i in range(3):
		if(i != num):
			arr[j] = i
			j += 1

	return arr

def setColors(num):
	color = np.array((0, 0, 0)) #create color array

	color[num] = 255 #set full color

	#pick and set other color
	choiceArray = createChoiceArray(num)
	pos = random.choice(choiceArray) #pick other color
	color[int(pos)] = random.randint(0, 255)

	return color

def runner(speed):
	#choose random color
	color = random_color()

	#make the next light change to that color with time delay
	for i in range(num_pixels):
		pixels[i] = color
		pixels.show()
		time.sleep(speed)

main()
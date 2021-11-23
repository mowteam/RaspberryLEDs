import neopixel
import time
from settings import num_pixels, pixels
from randomColorRainbow import random_color
def main():
	for i in range(num_pixels):
		#pixels[i] = random_color()
		pixels[i] = [255 - 2*i, 0, 100]
	pause = float(input("Speed/Pause Time: "))
	selectionSort(pause)

def value(color):
	return color[0]

def selectionSort(pause): #ascending order
	for i in range(num_pixels):
		time.sleep(pause)
		min_i = i
		for j in range(i+1, num_pixels - 1):
			if(value(pixels[j]) < value(pixels[min_i])): #if less than min set new min
				min_i = j
		#swap min and i
		swap(i, min_i)
		pixels.show()

def swap(index1, index2):
	temp = pixels[index1]
	pixels[index1] = pixels[index2]
	pixels[index2] = temp

main()

import neopixel
import numpy as np
from settings import num_pixels, pixels
from randomColorRainbow import random_color

def main():
	fibonacci = Fibonacci()

	index  = 0
	for x in fibonacci:
		print(str(index) + " x: " + str(x))
		color = random_color()
		for i in range(x):
			pixels[index + i] = color
		index = index + x
	pixels.show()

def readColor():
	color = input("Enter R, G, B: ")
	return tuple(int(x) for x in color.split(","))

def Fibonacci(): #array where each term represents a term in the fibonacci sequence
	arr = [0, 1]
	f = 0
	for sum in range(2, num_pixels):
		f = f + arr[sum - 1] + arr[sum - 2]
		if(f >= num_pixels):
			arr.append(num_pixels - 1 - (f - arr[sum - 1] - arr[sum - 2]))
			return arr
		arr.append(arr[sum-1] + arr[sum - 2])
	return arr

main()

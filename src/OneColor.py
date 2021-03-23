import board
import neopixel

#initialize pixels
pixel_pin = board.D18
num_pixels = 149
ORDER = neopixel.RGB 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER
)

i = input("Enter a color (as R, G, B): ")
color = tuple(int(x) for x in i.split(","))
pixels.fill(color)
pixels.show()
import board
import neopixel
import sys

#initialize
pixel_pin = board.D10
num_pixels = sys.argv[1]
ORDER = neopixel.RGB 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER
)

#turn LEDs off
pixels.fill(0, 0, 0)
pixels.show()
import board
import neopixel


#initialize pixels
pixel_pin = board.D18
num_pixels = 100
ORDER = neopixel.RGB
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER
)
import board
import neopixel

#initialize
pixel_pin = board.D10
num_pixels = 149
ORDER = neopixel.GRB 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER
)

#turn LEDs off
pixels.fill(0, 0, 0)
pixels.show()
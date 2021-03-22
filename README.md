# RaspberryLEDs
A collection of Python programs that can be run on a Raspberry pi to control individually addressable LED lights.

# Setup
I have a 3B+ Raspberry Pi connected to ws2811 LEDs through the GPIO18 pin. The LEDs are powered with a 5V 10A power supply.


# How to Write Programs
Controlling the LEDs relies on the neopixel and board python libraries. Each program must initalize a Neopixel Object, which requires the GPIO pin and the number of pixels as parameters. Additional parameters include the color ORDER (ex: RGB) and auto_write. More information about the neopixel library can be found <a href = 'https://circuitpython.readthedocs.io/projects/neopixel/en/latest/'>here</a>. Here is an example of how to initialize the Neopixel Object:

'''
import neopixel
import board

#initialize pixels
pixel_pin = board.D18
num_pixels = 149
ORDER = neopixel.RGB 
pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, auto_write=False, pixel_order=ORDER
)
'''

# Location of Pixels
At the moment, I have the LEDs taped to a board with no specific pattern in their position. However, I hope to plot their 2D position and provide these details in a txt file to be used in programs.

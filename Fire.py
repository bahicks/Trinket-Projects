# Light Ring V1
# Made By Joey Hicks
# Data made on Dec 3rd 2018

#import needed libraries
import time
import board
import neopixel

# define constants
PIXEL_PIN = board.D1
NUM_PIXELS = 16
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 50, 0)
GRAY = (128, 128, 128)
MAROON = (128, 0, 0)
FIREBRICK = (178, 34, 34)
PINK = (255, 20, 147)

# create neopixel object
pixels = neopixel.NeoPixel(PIXEL_PIN, NUM_PIXELS, brightness=1, auto_write=False)

# define subroutines / functions

# define odd_pixels - make odd pixels green and even pixels purple 
def odd_pixels():
	for i in range(NUM_PIXELS):
		if (i % 2) == 0:
			pixels[i] = RED
		else:
			pixels[i] = ORANGE

# define even_pixels
def even_pixels():
	for i in range (NUM_PIXELS):
		if (i % 2) == 0:
			pixels[i] = ORANGE
		else:
			pixels[i] = RED

#main routine
while True:
	odd_pixels()
	pixels.show()
	time.sleep(0.5)
	even_pixels()
	pixels.show()
	time.sleep(0.5)
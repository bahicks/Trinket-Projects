# CircuitPython demo - NeoPixel
# p.102 CircuitPython NeoPixel https://cdn-learn.adafruit.com/downloads/pdf/adafruit-trinket-m0-circuitpython-arduino.pdf

import time
import board
import neopixel

pixel_pin = board.D1
num_pixels = 16

RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = WHITE = (255, 255, 255)

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.1, auto_write=False)


# def color_chase(color, wait):
# 	for i in range(num_pixels):
# 		pixels[i] = color
# 		time.sleep(wait)
# 		pixels.show()
# 		time.sleep(0.5)
# 
# def rainbow_cycle(wait):
# 	for j in range(255):
# 		for i in range(num_pixels):
# 			rc_index = (i * 256 // num_pixels) + j
# 			pixels[i] = wheel(rc_index & 255)
# 			pixels.show()
# 			time.sleep(wait)
def odd_pixels(color, wait):
	for i in range(num_pixels):
		if (i % 2) == 0:
			pixels[i] = BLUE
		else:
			pixels[i] = WHITE
		# time.sleep(wait)
		
def even_pixels(color, wait):
	for i in range(num_pixels):
		if (i % 2) == 0:
			pixels[i] = WHITE
		else:
			pixels[i] = BLUE
		# time.sleep(wait)
		
				



while True:
#  	pixels.fill(RED)
#  	pixels.show()
#  	# Increase or decrease to change the speed of the solid color change.
#  	time.sleep(1)
#  	pixels.fill(GREEN)
#  	pixels.show()
#  	time.sleep(1)
#  	pixels.fill(BLUE)
#  	pixels.show()
#  	time.sleep(1)
# 
#  	color_chase(RED, 0.1) # Increase the number to slow down the color chase
#  	color_chase(YELLOW, 0.1)
#  	color_chase(GREEN, 0.1)
#  	color_chase(CYAN, 0.1)
#  	color_chase(BLUE, 0.1)
#  	color_chase(PURPLE, 0.1)
#  
#  	rainbow_cycle(0) # Increase the number to slow down the rainbow
	odd_pixels(BLUE, 0.1)
	pixels.show()
	time.sleep(1.0)
	even_pixels(WHITE, 0.1)
	pixels.show()
	time.sleep(01.0)
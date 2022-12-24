import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

strip.fill((72,209,204))

strip.write()
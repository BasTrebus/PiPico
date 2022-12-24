import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

strip[0] = (255,0,0)
strip[1] = (255,0,0)
strip[2] = (255,0,0)
strip[3] = (255,0,0)
strip[4] = (255,0,0)

strip.write()
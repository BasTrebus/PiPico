import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0
pink = 255,20,147

for i in range(15):

    strip[i] = (green)

strip.write()
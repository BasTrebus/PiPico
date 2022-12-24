import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

red = 255,0,0
green = 0,255,0
blue = 0,0,255

colors = [red, green, blue]

while True:

    for j in colors:

        for i in range(15):

            strip[i] = (j)

            time.sleep(0.1)

            strip.write()
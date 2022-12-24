import time
from machine import Pin
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

button = Pin(15, Pin.IN, Pin.PULL_DOWN)

red = 255,0,0
green = 0,255,0
blue = 0,0,255

colors = [red, green, blue]

myIndex = 0

indexLength = len(colors) -1

while True:

    time.sleep(0.4)

    if button.value() == 1:

        if myIndex < indexLength:

            myIndex = myIndex + 1

        else:

            myIndex = 0

        strip.fill((colors[myIndex]))

        strip.write()
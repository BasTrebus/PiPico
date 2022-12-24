import time
from machine import Pin, ADC
from neopixel import NeoPixel

strip = NeoPixel(Pin(28), 15)

potentiometer = ADC(Pin(26))

red = 255,0,0
green = 0,255,0
blue = 0,0,255

colors = [red, green, blue]

while True:

    for j in colors:

        for i in range(15):

            strip[i] = (j)

            myDelay = potentiometer.read_u16() / 50000
            time.sleep(myDelay)

            strip.write()

            print(myDelay)
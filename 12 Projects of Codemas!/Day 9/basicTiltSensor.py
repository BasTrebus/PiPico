from machine import Pin
import time

tilt  = Pin(26, Pin.IN, Pin.PULL_DOWN)

while True:

    time.sleep(0.01)

    if tilt.value() == 1:

        print("I tilted!")
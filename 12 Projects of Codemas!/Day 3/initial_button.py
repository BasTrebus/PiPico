from machine import Pin
import time

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)

while True:
    time.sleep(0.2)
    if button1.value() == 1:
        print("Button 1 pressed")
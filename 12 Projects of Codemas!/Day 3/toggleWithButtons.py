from machine import Pin
import time

button1 = Pin(13, Pin.IN, Pin.PULL_DOWN)

red = Pin(18, Pin.OUT)

while True:

    time.sleep(0.5)
    
    if button1.value() == 1:

        print("Button 1 is pressed")

        red.toggle()
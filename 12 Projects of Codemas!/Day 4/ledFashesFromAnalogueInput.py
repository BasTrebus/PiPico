from machine import ADC, Pin
import time

potentiometer = ADC(Pin(27))

red = Pin(18, Pin.OUT)

myDelay = 0

while True:

    myDelay = potentiometer.read_u16() / 65000

    red.value(1)
    time.sleep(myDelay)

    red.value(0)
    time.sleep(myDelay)
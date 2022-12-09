from machine import ADC, Pin
import time

potentiometer = ADC(Pin(27))

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

reading = 0

while True:

    reading = potentiometer.read_u16()

    print(reading)

    time.sleep(0.1)

    if reading <= 20000:

        red.value(1)
        amber.value(0)
        green.value(0)

    elif 20000 < reading < 40000:

        red.value(0)
        amber.value(1)
        green.value(0)

    if reading >= 40000:

        red.value(0)
        amber.value(0)
        green.value(1)
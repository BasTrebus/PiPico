from machine import ADC, Pin
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

lightSensor = ADC(Pin(26))

while True:

    light = lightSensor.read_u16()

    lightPercent = round(light/65535*100, 1)

    print(str(lightPercent) + "%")

    time.sleep(1)

    if lightPercent <= 30:

        red.value(1)
        amber.value(0)
        green.value(0)


    if 30 < lightPercent < 60:

        red.value(0)
        amber.value(1)
        green.value(0)


    if lightPercent >= 60:

        red.value(0)
        amber.value(0)
        green.value(1)

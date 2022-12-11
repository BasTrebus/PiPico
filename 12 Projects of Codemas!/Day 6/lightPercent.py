from machine import ADC, Pin
from time import sleep

lightSensor = ADC(Pin(26))

light = lightSensor.read_u16()

lightPercent = round(light/65535*100, 1)

print(str(lightPercent) + "%")
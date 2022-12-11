from machine import ADC, Pin

lightSensor = ADC(Pin(26))

light = lightSensor.read_u16()

print(light)
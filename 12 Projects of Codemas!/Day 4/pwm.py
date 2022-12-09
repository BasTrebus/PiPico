from machine import ADC, Pin, PWM
import time

potentiometer = ADC(Pin(27))

led = PWM(Pin(18))

led.freq(1000)

reading = 0

while True:

    reading = potentiometer.read_u16()

    print(reading)

    led.duty_u16(reading)

    time.sleep(0.0001)
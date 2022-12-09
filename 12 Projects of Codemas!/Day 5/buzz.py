from machine import Pin, PWM
import time

buzzer = PWM(Pin(13))

buzzer.freq(1000)

buzzer.duty_u16(10000)

time.sleep(1)

buzzer.duty_u16(0)
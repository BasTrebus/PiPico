from machine import Pin, PWM
import time

buzzer = PWM(Pin(13))

C = 523
D = 587
E = 659
G = 784

volume = 10000

buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.5)

buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.5)

buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

buzzer.duty_u16(volume)
buzzer.freq(G)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

buzzer.duty_u16(volume)
buzzer.freq(C)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

buzzer.duty_u16(volume)
buzzer.freq(D)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

buzzer.duty_u16(volume)
buzzer.freq(E)
time.sleep(0.1)
buzzer.duty_u16(0)
time.sleep(0.2)

buzzer.duty_u16(0)
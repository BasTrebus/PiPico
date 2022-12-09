from machine import Pin, PWM
import time

buzzer = PWM(Pin(13))

C = 523
D = 587
E = 659
G = 784

volume = 32768

def playTone(note, vol, delay1, delay2):
    buzzer.duty_u16(vol)
    buzzer.freq(note)
    time.sleep(delay1)
    buzzer.duty_u16(0)
    time.sleep(delay2)

playTone(E, volume, 0.1, 0.2)
playTone(E, volume, 0.1, 0.2)
playTone(E, volume, 0.1, 0.5)

playTone(E, volume, 0.1, 0.2)
playTone(E, volume, 0.1, 0.2)
playTone(E, volume, 0.1, 0.5)

playTone(E, volume, 0.1, 0.2)
playTone(G, volume, 0.1, 0.2)
playTone(C, volume, 0.1, 0.2)
playTone(D, volume, 0.1, 0.2)
playTone(E, volume, 0.1, 0.2)

buzzer.duty_u16(0)
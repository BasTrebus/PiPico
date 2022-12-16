from machine import Pin, PWM
import time

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

buzzer = PWM(Pin(13))

buzzer.duty_u16(0)

pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

print("Warming up...")
time.sleep(10)
print("Sensor ready!")

def alarm():

    buzzer.duty_u16(8000)

    for i in range(5):

        buzzer.freq(5000)

        red.value(1)
        amber.value(1)
        green.value(1)

        time.sleep(1)

        buzzer.freq(500)

        red.value(0)
        amber.value(0)
        green.value(0)

        time.sleep(1)

    buzzer.duty_u16(0)

while True:

    time.sleep(0.01)

    if pir.value() == 1:

        print("I SEE YOU!!")

        alarm()

        print("Sensor active")

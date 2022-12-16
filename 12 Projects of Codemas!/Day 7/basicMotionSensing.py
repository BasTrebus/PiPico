from machine import Pin
import time

pir = Pin(26, Pin.IN, Pin.PULL_DOWN)

print("Warming up...")

time.sleep(10)

print("Sensor Ready")

while True:

    time.sleep(0.01)

    if pir.value() == 1:

        print("I SEE YOU!")

        time.sleep(5)

        print("Sensor Active")
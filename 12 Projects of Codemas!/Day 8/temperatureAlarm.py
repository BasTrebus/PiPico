import onewire, ds18x20, time
from machine import Pin, PWM

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

buzzer = PWM(Pin(13))
buzzer.duty_u16(0)

SensorPin = Pin(26, Pin.IN)
sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))
roms = sensor.scan()

def alarm():

    buzzer.duty_u16(10000)

    for i in range(5):

        buzzer.freq(5000)

        red.value(1)
        amber.value(1)
        green.value(1)

        time.sleep(0.4)

        buzzer.freq(1000)

        red.value(0)
        amber.value(0)
        green.value(0)

        time.sleep(0.4)

    buzzer.duty_u16(0)

while True:

    time.sleep(5)

    for rom in roms:

        sensor.convert_temp()
        time.sleep(1)

        reading = sensor.read_temp(rom)

        print(reading)

        if reading < 18:

            alarm()
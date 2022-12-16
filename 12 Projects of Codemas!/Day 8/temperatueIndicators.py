import onewire, ds18x20, time
from machine import Pin

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

SensorPin = Pin(26, Pin.IN)

sensor = ds18x20.DS18X20(onewire.OneWire(SensorPin))

roms = sensor.scan()

while True:

    time.sleep(5)

    for rom in roms:

        sensor.convert_temp()
        time.sleep(1)

        reading = sensor.read_temp(rom)

        print(reading)

        if reading <= 18:

            red.value(1)
            amber.value(0)
            green.value(0)

        elif 18 < reading < 22:

            red.value(0)
            amber.value(1)
            green.value(0)

        elif reading >= 22:

            red.value(0)
            amber.value(0)
            green.value(1)

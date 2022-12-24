from machine import Pin, PWM
import time, sys

red = Pin(18, Pin.OUT)
amber = Pin(19, Pin.OUT)
green = Pin(20, Pin.OUT)

beam = Pin(26, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(13))
buzzer.freq(1000)
buzzer.duty_u16(0)

startTime = 0
timeCheck = 0
scoreCounter = 0
state = 0
targetScore = 100

print("Game starts after the beep!")

buzzer.duty_u16(10000)
time.sleep(2)
buzzer.duty_u16(0)

print("GO!")
print("-----------------------------------------------")

startTime = time.time()

while True:

    time.sleep(0.0001)

    timeCheck = time.time() - startTime

    if timeCheck >= 30:

        red.value(0)
        amber.value(0)
        green.value(0)

        buzzer.duty_u16(10000)
        time.sleep(0.2)
        buzzer.duty_u16(0)

        print("-----------------------------------------------")
        print("GAME OVER! YOU LOSE :(")
        print("The target was", targetScore, ", you scored", scoreCounter)
        print("-----------------------------------------------")

        sys.exit()

    elif scoreCounter >= targetScore:

        red.value(0)
        amber.value(0)
        green.value(0)

        buzzer.duty_u16(10000)
        time.sleep(0.2)
        buzzer.duty_u16(0)

        print("-----------------------------------------------")
        print("YOU WIN")
        print("You took", timeCheck, "seconds!")
        print("-----------------------------------------------")

        sys.exit()

    elif state == 0 and beam.value() == 0:

        scoreCounter = scoreCounter + 1

        state = 1

        print("SCORE =", scoreCounter, "/", targetScore)
        print("Time remaining:", (30 - timeCheck))

        if scoreCounter < (targetScore *0.33 ):

            red.value(1)
            amber.value(0)
            green.value(0)

        elif (targetScore * 0.33 ) < scoreCounter < (targetScore * 0.67):

            red.value(0)
            amber.value(1)
            green.value(0)

        elif (scoreCounter > targetScore * 0.67):

            red.value(0)
            amber.value(0)
            green.value(1)

    elif state == 1 and beam.value() == 1:

        state = 0
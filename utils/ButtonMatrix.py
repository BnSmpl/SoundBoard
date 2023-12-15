# Code to test button matrix
# Will print every key input

import RPi.GPIO as GPIO
import time

L1 = 5
L2 = 6
L3 = 13
L4 = 19

C1 = 12
C2 = 16
C3 = 20
C4 = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(L1, GPIO.OUT)
GPIO.setup(L2, GPIO.OUT)
GPIO.setup(L3, GPIO.OUT)
GPIO.setup(L4, GPIO.OUT)

GPIO.setup(C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if GPIO.input(C1) == 1:
        return characters[0]
    if GPIO.input(C2) == 1:
        return characters[1]
    if GPIO.input(C3) == 1:
        return characters[2]
    if GPIO.input(C4) == 1:
        return characters[3]
    GPIO.output(line, GPIO.LOW)


def listener():
    try:
        while True:
            charactersL1 = readLine(L1, ["ahhhh.mp3", "beback.mp3", "boom.mp3", "A"])
            charactersL2 = readLine(L2, ["bruh.mp3", "calming.mp3", "clap.mp3", "B"])
            charactersL3 = readLine(L3, ["gae.mp3", "giveuup.mp3", "lenz.mp3", "C"])
            charactersL4 = readLine(L4, ["*", "0", "#", "D"])
            time.sleep(0.1)
            if charactersL1:
                return charactersL1
            if charactersL2:
                return charactersL2
            if charactersL3:
                return charactersL3
            if charactersL4:
                return charactersL4
    except KeyboardInterrupt:
        print("\nBye bye!")

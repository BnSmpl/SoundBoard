# Code to test button matrix
# Will print every key input

import RPi.GPIO as GPIO
import time
from mpyg321.mpyg321 import MPyg321Player

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


def play_mp3(file_path):
    player = MPyg321Player()
    player.play_song(file_path)
    while True:
        time.sleep(1)


def readLine(line, characters):
    GPIO.output(line, GPIO.HIGH)
    if GPIO.input(C1) == 1:
        print(characters[0])
        play_mp3('/Sounds/lenz.mp3')
    if GPIO.input(C2) == 1:
        print(characters[1])
    if GPIO.input(C3) == 1:
        print(characters[2])
    if GPIO.input(C4) == 1:
        test = characters[3]
        if test == 'A':
            print('i should be recording new audio now')
        if test == 'B':
            print('i think i should be recording a sequence now')
        if test == 'C':
            print('idk what i should be doing')
        if test == 'D':
            print('i\'m D')
    GPIO.output(line, GPIO.LOW)


try:
    while True:
        readLine(L1, ["1", "2", "3", "A"])
        readLine(L2, ["4", "5", "6", "B"])
        readLine(L3, ["7", "8", "9", "C"])
        readLine(L4, ["*", "0", "#", "D"])
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nBye bye!")

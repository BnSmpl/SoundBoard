from mpyg321.mpyg321 import MPyg321Player
import time


def play_mp3(signal):
    print(signal)
    soundPath = './Sounds/'
    player = MPyg321Player()
    player.play_song(soundPath + signal)
    while True:
        time.sleep(1)

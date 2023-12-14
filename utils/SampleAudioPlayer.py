from mpyg321.mpyg321 import MPyg321Player
import time


def play_mp3(mp3):
    print(mp3)
    soundPath = './Sounds/'
    player = MPyg321Player()
    player.play_song(soundPath + mp3)
    while True:
        time.sleep(1)

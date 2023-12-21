from mpyg321.mpyg321 import MPyg321Player
import time


def play_mp3(mp3):
    # Path der Audiodateien definieren
    soundPath = './Sounds/'

    print('Currently playing: "' + mp3 + '" ♬')

    # Audioplayer initailisieren und dann den entsprechenden Sound abspielen
    player = MPyg321Player()
    player.play_song(soundPath + mp3)
    time.sleep(.5)

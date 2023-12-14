from mpyg321.mpyg321 import MPyg321Player
import time

def play_mp3(file_path):
    player = MPyg321Player()
    player.play_song(file_path)
    while True:
        time.sleep(1)

if __name__ == "__main__":
    file_path = "lenz.mp3"
    play_mp3(file_path)

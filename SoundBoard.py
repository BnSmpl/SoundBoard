from utils.ButtonMatrix import listener
from utils.SampleAudioPlayer import play_mp3


def main():
    while True:
        play_mp3(listener())

from utils.ButtonMatrix import listener
from utils.SampleAudioPlayer import play_mp3


def main():
    try:
        while True:
            play_mp3(listener())
    except KeyboardInterrupt:
        print("\nBye bye!")


main()
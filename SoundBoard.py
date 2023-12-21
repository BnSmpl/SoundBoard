from utils.ButtonMatrix import listener
from utils.AudioPlayer import play_mp3


# Main Methode, welche in einer Dauerschleife läuft,
# bis das Programm durch Keyboard-Interrupt gestoppt wird.
def main():
    while True:
        # Starten des mp3 Players und des Listeners der Buttons
        play_mp3(listener())


# Starten der main Methode
main()

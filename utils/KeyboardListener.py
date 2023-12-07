import sys
import tty
import termios
from utils.Signals import Signals
from signalType import signalType

key_to_signal = {
    '1': signalType.SOUND1,
    '2': signalType.SOUND2,
    '3': signalType.SOUND3,
    '4': signalType.SOUND4,
    '5': signalType.SOUND5,
    '6': signalType.SOUND6,
    '7': signalType.SOUND7,
    '8': signalType.SOUND8,
    '9': signalType.SOUND9,

    'r': signalType.REC_BTN,
    's': signalType.STOP_SOUND,
    'q': signalType.QUIT
}


def listen_for_key():
    """
    Listens for a single key press and returns the corresponding Signal.
    Returns None if the key is not mapped to a signal.
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

    return Signals(key_to_signal[ch]) if ch in key_to_signal else None

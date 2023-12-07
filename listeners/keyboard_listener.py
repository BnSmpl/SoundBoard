import sys
import tty
import termios
from utils.signals import Signal, SignalType

key_to_signal = {
    '1': SignalType.SOUND1,
    '2': SignalType.SOUND2,
    '3': SignalType.SOUND3,
    '4': SignalType.SOUND4,
    '5': SignalType.SOUND5,
    '6': SignalType.SOUND6,
    '7': SignalType.SOUND7,
    '8': SignalType.SOUND8,
    '9': SignalType.SOUND9,

    'r': SignalType.REC_BTN,
    's': SignalType.STOP_SOUND,
    'q': SignalType.QUIT
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

    return Signal(key_to_signal[ch]) if ch in key_to_signal else None

from enum import Enum, auto


class SignalType(Enum):
    SOUND1 = auto()
    SOUND2 = auto()
    SOUND3 = auto()
    SOUND4 = auto()
    SOUND5 = auto()
    SOUND6 = auto()
    SOUND7 = auto()
    SOUND8 = auto()
    SOUND9 = auto()

    REC_BTN = auto()
    QUIT = auto()
    STOP_SOUND = auto()


class Signals:
    def __init__(self, signal_type, data=None):
        if not isinstance(signal_type, SignalType):
            raise ValueError("Invalid signal type")
        self.signal_type = signal_type
        self.data = data

    def is_type(self, type):
        return self.signal_type == type

    def __str__(self):
        return f"Signal(type={self.signal_type}, data={self.data})"


"""
Example usage
signal = Signal(SignalType.SOUND1, data={"volume": 5})
print(signal)  # Signal(type=SignalType.SOUND1, data={'volume': 5})
"""

from signalType import signalType


class Signals:
    def __init__(self, signal_type, data=None):
        if not isinstance(signal_type, signalType):
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

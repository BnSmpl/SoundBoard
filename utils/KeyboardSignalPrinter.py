# Is used to test the keyboard listener. It prints the signal type when a signal is received.

from KeyboardListener import listen_for_key
from utils.Signals import SignalType


def process_signal(signal):
    """
    Processes the given signal and prints the signal type.

    Args:
    signal (Signal): The signal to process.
    """
    if signal:
        print(f"Received signal: {signal.signal_type.name}")
        if signal.signal_type == SignalType.QUIT:
            return True
    return False


def main():
    print("Program is running. Press 'q' to exit.")

    try:
        while True:
            # Listen for keyboard signals
            keyboard_signal = listen_for_key()

            # Process the keyboard signal
            if keyboard_signal:
                print(f"Keyboard Signal Received: {keyboard_signal.signal_type.name}")
                if process_signal(keyboard_signal):
                    break

    except KeyboardInterrupt:
        print("Exiting the program.")

    print("Program exited.")


if __name__ == "__main__":
    main()
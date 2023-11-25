import sys
import tty
import termios
from soundDict import sounds
from listeners.keyboard_listener import listen_for_key
from utils.signals import Signal, SignalType

try:
    print("Program is running. Press 'q' to exit.")
    while True:
        signal = listen_for_key()
        if signal:
        
            if signal.signal_type == SignalType.QUIT:  # Exit condition
                break
            # Process other signals as needed
            print(f"Signal received: {signal.signal_type}")
except KeyboardInterrupt:
    print("Exiting the program.")

print("Program exited.")
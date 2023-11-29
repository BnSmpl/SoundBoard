from soundDict import sounds
from listeners.keyboard_listener import listen_for_key
from utils.signals import Signal, SignalType

try:
    print("Program is running. Press 'q' to exit.")
    while True:
        
        signal = listen_for_key()
        if signal and signal.signal_type != SignalType.QUIT:
            print(signal.signal_type.name + " | " + sounds.get(signal.signal_type.name))  # Debugging
            # sound_file = sounds.get(signal.signal_type.name, None)
        elif signal and signal.signal_type == SignalType.QUIT:
            break
        
except KeyboardInterrupt:
    print("Exiting the program.")

print("Program exited.")
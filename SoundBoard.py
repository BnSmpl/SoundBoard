from soundDict import sounds
from listeners.keyboard_listener import listen_for_key
from utils.signals import Signal, SignalType

try:
    print("Program is running. Press 'q' to exit.")
    while True:
        
        signal = listen_for_key()
        print("Received signal:", signal)  # Debugging statement
        if signal and signal.signal_type != SignalType.QUIT:
            print("Looking for sound file for signal type:", signal.signal_type.name)  # Debugging
            sound_file = sounds.get(signal.signal_type.name, None)
            if sound_file:
                print(sound_file)
            else:
                print("No sound mapped for this signal.")
        elif signal and signal.signal_type == SignalType.QUIT:
            break
        
except KeyboardInterrupt:
    print("Exiting the program.")

print("Program exited.")
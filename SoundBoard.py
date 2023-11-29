import threading
from soundDict import sounds
from listeners.keyboard_listener import listen_for_key
from listeners.gpio_listener import GPIOListener, SignalType

# Initialize GPIO listener
gpio_to_signal = {
    26: SignalType.SOUND1,
    # ... other mappings ...
    7: SignalType.SOUND9
}
gpio_listener = GPIOListener(gpio_to_signal)

def gpio_thread_function():
    """
    Function to be run by the GPIO listener thread.
    """
    gpio_listener.listen()

def process_signal(signal):
    """
    Processes the given signal, playing the corresponding sound.
    """
    print("Received signal:", signal)  # Debugging statement
    print("sounds dictionary:", sounds)
    if signal and signal.signal_type != SignalType.QUIT:
        print("Looking for sound file for signal type:", signal.signal_type.name)  # Debugging
        sound_file = sounds.get(signal.signal_type.name, None)
        if sound_file:
            print(sound_file)  # Play sound
        else:
            print("No sound mapped for this signal.")
    elif signal and signal.signal_type == SignalType.QUIT:
        return True
    return False

def main():
    print("Program is running. Press 'q' to exit.")

    # Start GPIO listener in a separate thread
    gpio_thread = threading.Thread(target=gpio_thread_function)
    gpio_thread.start()

    try:
        while True:
            signal = listen_for_key()
            if process_signal(signal):
                break
    except KeyboardInterrupt:
        print("Exiting the program.")
    finally:
        gpio_thread.join()  # Ensure GPIO thread is properly closed

    print("Program exited.")

if __name__ == "__main__":
    main()

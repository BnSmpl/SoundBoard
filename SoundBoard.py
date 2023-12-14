import queue
import sys
import threading
from SoundDict import sounds
from utils.KeyboardListener import listen_for_key
from utils.GPIOListener import start_gpio_listener
from utils.SampleAudioPlayer import play_mp3
import utils.SignalType as SignalType
from utils.GPIOSignalPrinter import process_signals

sys.path.insert(0, "..")

# Function to process signals
def process_signal(signal):
    if signal and signal.signal_type != SignalType.QUIT:
        sound_info = signal.signal_type.name + " | " + sounds.get(signal.signal_type.name)
        print(sound_info)  # Replace this with actual sound playing logic
    elif signal and signal.signal_type == SignalType.QUIT:
        return True
    return False
  
def main():
    print("Program is running. Press 'q' to exit.")

    # Shared queue for signals
    signal_queue = queue.Queue()
    
    # Start GPIO listener in a separate thread
    gpio_thread = threading.Thread(target=start_gpio_listener, args=(signal_queue,))
    gpio_thread.start()
    
    process_signals(signal_queue)

    try:
        while True:
            # Check for and process any signals in the queue
            try:
                signal = signal_queue.get_nowait()
                if process_signal(signal):
                    play_mp3(signal)
                    break
            except queue.Empty:
                pass

            # Also check for keyboard signals
            keyboard_signal = listen_for_key()
            if keyboard_signal:
                signal_queue.put(keyboard_signal)

    except KeyboardInterrupt:
        print("Exiting the program.")

    finally:
        gpio_thread.join()  # Ensure GPIO thread is properly closed

    print("Program exited.")

if __name__ == "__main__":
    main()

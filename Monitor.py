import threading
import queue
from listeners.keyboard_listener import listen_for_key
from utils.signals import SignalType
from gpio_listener import GPIOListener, start_gpio_listener  # Import the GPIO listener

def process_signal(signal):
    # ... [Same as before] ...

def main():
    print("Program is running. Press 'q' to exit.")

    signal_queue = queue.Queue()  # Queue for inter-thread communication

    # Start GPIO listener in a new thread
    gpio_thread = threading.Thread(target=start_gpio_listener, args=(signal_queue,))
    gpio_thread.start()

    try:
        while True:
            # Listen for keyboard signals
            keyboard_signal = listen_for_key()

            # Process the keyboard signal
            if keyboard_signal:
                print(f"Keyboard Signal Received: {keyboard_signal.signal_type.name}")
                if process_signal(keyboard_signal):
                    break

            # Check if there is a signal from GPIO
            while not signal_queue.empty():
                gpio_signal = signal_queue.get()
                print(f"GPIO Signal Received: {gpio_signal.signal_type.name}")
                if process_signal(gpio_signal):
                    break

    except KeyboardInterrupt:
        print("Exiting the program.")

    gpio_thread.join()  # Ensure the GPIO listener thread is also closed
    print("Program exited.")

if __name__ == "__main__":
    main()

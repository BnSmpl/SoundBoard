import threading
import queue
from listeners.gpio_listener import start_gpio_listener, SignalType

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
    print("Program is running. Press Ctrl+C to exit.")

    signal_queue = queue.Queue()  # Queue for inter-thread communication

    # Start GPIO listener in a new thread
    gpio_thread = threading.Thread(target=start_gpio_listener, args=(signal_queue,))
    gpio_thread.start()

    try:
        while True:
            # Check if there is a signal from GPIO
            if not signal_queue.empty():
                gpio_signal = signal_queue.get()
                print(f"GPIO Signal Received: {gpio_signal.signal_type.name}")
                if process_signal(gpio_signal):
                    break

    except KeyboardInterrupt:
        print("Exiting the program.")

    finally:
        gpio_thread.join()  # Ensure the GPIO listener thread is also closed
        print("Program exited.")

if __name__ == "__main__":
    main()
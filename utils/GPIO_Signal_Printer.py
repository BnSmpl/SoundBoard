# is used to test the GPIO listener. It prints the signal type when a signal is received.

import queue
import threading
from listeners.gpio_listener import start_gpio_listener


def process_signals(signal_queue):
    try:
        while True:
            # Wait for a signal to be available in the queue
            signal = signal_queue.get()
            print(f"Received Signal: {signal}")
    except KeyboardInterrupt:
        print("Signal processing interrupted.")


if __name__ == "__main__":
    # Create a queue for inter-thread communication
    signal_queue = queue.Queue()

    # Start the GPIO listener in a separate thread
    listener_thread = threading.Thread(target=start_gpio_listener, args=(signal_queue,))
    listener_thread.start()

    print("GPIO Listener started. Waiting for signals...")

    # Start processing signals
    process_signals(signal_queue)

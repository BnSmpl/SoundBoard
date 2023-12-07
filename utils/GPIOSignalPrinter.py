# is used to test the GPIO listener. It prints the signal type when a signal is received.

import queue
import threading
from GPIOListener import start_gpio_listener


def process_signals(signal_queue):
    try:
        while True:
            # Wait for a signal to be available in the queue
            signal = signal_queue.get()
            print(f"Received Signal: {signal}")
    except KeyboardInterrupt:
        print("Signal processing interrupted.")

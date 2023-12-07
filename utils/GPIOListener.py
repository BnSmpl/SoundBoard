# Listens for GPIO signals and returns the corresponding Signal.

import sys
import os
import RPi.GPIO as GPIO
import time
from Signals import Signals, SignalType


class GPIOListener:
    def __init__(self, gpio_to_signal, signal_queue, debounce_time=0.1):
        """
        Initializes the GPIOListener with specified GPIO to signal mappings.

        Args:
        gpio_to_signal (dict): A dictionary mapping GPIO ports to SignalTypes.
        signal_queue (queue.Queue): Queue for inter-thread communication.
        debounce_time (float): Debounce time in seconds.
        """
        self.gpio_to_signal = gpio_to_signal
        self.signal_queue = signal_queue
        self.debounce_time = debounce_time
        self.last_signal_time = {port: 0 for port in gpio_to_signal}
        self.setup_gpio()

    def setup_gpio(self):  # Sets up the GPIO system for the specified ports.
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for port in self.gpio_to_signal.keys():
            GPIO.setup(port, GPIO.IN)

    def generate_signal(self, port):
        """
        Checks specified GPIO ports and generates a signal if the port is active.
        Args: port (int): The GPIO port to check.
        Returns: Signal object if the port is active, None otherwise.
        """
        current_time = time.time()
        if not GPIO.input(port) and (current_time - self.last_signal_time[port] > self.debounce_time):
            self.last_signal_time[port] = current_time
            return Signals(self.gpio_to_signal[port])
        return None

    def listen(self):  # Continuously monitors GPIO ports and generates signals.
        try:
            while True:
                for port in self.gpio_to_signal.keys():
                    signal = self.generate_signal(port)
                    if signal:
                        self.signal_queue.put(signal)
                        # Process the signal as needed
                        # print(f"Signal Generated: {signal}")
                time.sleep(0.5)  # Polling interval
        except KeyboardInterrupt:
            print("GPIO listener interrupted. Cleaning up...")
        finally:
            GPIO.cleanup()


def start_gpio_listener(signal_queue):
    """
    Initializes and starts the GPIO listener.
    
        Args:
    signal_queue (queue.Queue): Queue for inter-thread communication.
    """
    gpio_to_signal = {
        26: SignalType.SOUND1,
        13: SignalType.SOUND2,
        19: SignalType.SOUND3,
        6: SignalType.SOUND4,
        5: SignalType.SOUND5,
        20: SignalType.SOUND6,
        21: SignalType.SOUND7,
        12: SignalType.SOUND8,
        7: SignalType.SOUND9
    }
    listener = GPIOListener(gpio_to_signal, signal_queue)
    listener.listen()

import RPi.GPIO as GPIO
import time
from signals import Signal, SignalType

class GPIOListener:
    def __init__(self, gpio_to_signal):
        """
        Initializes the GPIOListener with specified GPIO to signal mappings.

        Args:
        gpio_to_signal (dict): A dictionary mapping GPIO ports to SignalTypes.
        """
        self.gpio_to_signal = gpio_to_signal
        self.setup_gpio()

    def setup_gpio(self):
        """
        Sets up the GPIO system for the specified ports.
        """
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        for port in self.gpio_to_signal.keys():
            GPIO.setup(port, GPIO.IN)

    def generate_signal(self, port):
        """
        Checks the specified GPIO port and generates a signal if the port is active.

        Args:
        port (int): The GPIO port to check.

        Returns:
        Signal: The generated Signal object if the port is active, None otherwise.
        """
        if GPIO.input(port):
            return Signal(self.gpio_to_signal[port])
        return None

    def listen(self):
        """
        Main method to continuously monitor GPIO ports and generate signals.
        """
        try:
            while True:
                for port in self.gpio_to_signal.keys():
                    signal = self.generate_signal(port)
                    if signal:
                        # Process the signal as needed
                        print(f"Signal Generated: {signal}")
                time.sleep(0.1)  # Polling interval
        except KeyboardInterrupt:
            print("GPIO listener interrupted. Cleaning up...")
        finally:
            GPIO.cleanup()

if __name__ == "__main__":
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


    listener = GPIOListener(gpio_to_signal)
    listener.listen()

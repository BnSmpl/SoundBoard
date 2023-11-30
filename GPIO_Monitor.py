import RPi.GPIO as GPIO
import time
import threading
import queue
from utils.signals import Signal, SignalType

class GPIOListener:
    # ... [Your GPIOListener class as before]

def start_gpio_listener(signal_queue):
    # ... [Your start_gpio_listener function as before]

# Setting up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO ports and corresponding signal types
gpio_to_signal = {
    26: SignalType.SOUND1,
    13: SignalType.SOUND2,
    19: SignalType.SOUND3,
    6:  SignalType.SOUND4,
    5:  SignalType.SOUND5,
    20: SignalType.SOUND6,
    21: SignalType.SOUND7,
    12: SignalType.SOUND8,
    7:  SignalType.SOUND9
}

# Initialize port status
port_status = {port: False for port in gpio_to_signal}  # False indicates no signal
debounce_time = 0.1  # Adjust as needed

# Function to update and check port status
def check_and_update_port_status():
    for port in gpio_to_signal:
        current_status = GPIO.input(port)
        last_status = port_status[port]
        current_time = time.time()

        if current_status != last_status and current_time - last_stable_time[port] > debounce_time:
            port_status[port] = current_status
            last_stable_time[port] = current_time
            if current_status:
                # Generate and queue a signal if the port status is high
                signal = Signal(gpio_to_signal[port])
                signal_queue.put(signal)

# Main function
def main():
    print("GPIO Monitoring started. Press CTRL+C to exit.")

    # Set up signal queue and start GPIO listener thread
    signal_queue = queue.Queue()
    gpio_listener_thread = threading.Thread(target=start_gpio_listener, args=(signal_queue,))
    gpio_listener_thread.start()

    try:
        while True:
            check_and_update_port_status()
            time.sleep(0.1)  # Polling interval

            # Process any queued signals
            while not signal_queue.empty():
                signal = signal_queue.get()
                print(f"Signal Received: {signal.signal_type.name}")

    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        GPIO.cleanup()  # Clean up GPIO on exit
        gpio_listener_thread.join()  # Ensure the listener thread exits cleanly

if __name__ == "__main__":
    main()

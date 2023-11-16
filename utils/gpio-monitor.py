# requirements: pip3 install RPi.GPIO

# This script monitors the GPIO ports of a Raspberry Pi Model 4. If the port input is high it prints "x", if it is low it prints nothing.
# To exit the script, press CTRL+C

import RPi.GPIO as GPIO
import time
import signal
import sys
import os

# Setting up GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom SOC channel numbering
GPIO.setwarnings(False)

# List of GPIO ports you want to monitor
gpio_ports = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]

# Set up ports as input and initialize their status
port_status = {}
last_stable_time = {}
debounce_time = 0.05  # Time in seconds to wait for a stable port status
for port in gpio_ports:
    GPIO.setup(port, GPIO.IN)
    port_status[port] = GPIO.input(port)
    last_stable_time[port] = time.time()

def print_gpio_status():
    print("GPIO Port Status")
    print("Port\tStatus")
    for port, status in port_status.items():
        status_char = '' if status else 'X'
        print(f"{port}\t{status_char}")
        
def clear_console():
    os.system('clear') # clears the console screen 

def signal_handler(sig, frame):
    print("\nExiting...")
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

use_debouncing = False # Set to False to disable debouncing

try:
    while True:
        changed = False
        for port in gpio_ports:
            current_status = GPIO.input(port)
            current_time = time.time()

            if use_debouncing:
                if current_status != port_status[port] and current_time - last_stable_time[port] >= debounce_time:
                    port_status[port] = current_status
                    last_stable_time[port] = current_time
                    changed = True
                elif current_status != port_status[port]:
                    last_stable_time[port] = current_time
            else:
                if current_status != port_status[port]:
                    port_status[port] = current_status
                    changed = True

        if changed:
            clear_console() # clears console before printing new status
            print_gpio_status()

        time.sleep(0.1)  # Check for changes every 100ms

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    GPIO.cleanup()  # Reset GPIO ports used in this script
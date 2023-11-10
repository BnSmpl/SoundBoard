# requirements: pip3 install keyboard RPi.GPIO

# This script monitors the GPIO ports. If the port input is high it prints "x", if it is low it prints nothing.
# To exit the script, press CTRL+C

import RPi.GPIO as GPIO
import time
import signal
import sys

# Setting up GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom SOC channel numbering
GPIO.setwarnings(False)

# List of GPIO ports you want to monitor
gpio_ports = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]

# Set up ports as input and initialize their status
port_status = {}
for port in gpio_ports:
    GPIO.setup(port, GPIO.IN)
    port_status[port] = GPIO.input(port)

def print_gpio_status():
    print("GPIO Port Status")
    print("Port\tStatus")
    for port, status in port_status.items():
        status_char = 'X' if status else ''
        print(f"{port}\t{status_char}")

def signal_handler(sig, frame):
    print("\nExiting...")
    GPIO.cleanup()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    while True:
        changed = False
        for port in gpio_ports:
            current_status = GPIO.input(port)
            if port_status[port] != current_status:
                port_status[port] = current_status
                changed = True

        if changed:
            print_gpio_status()

        time.sleep(0.1)  # Check for changes every 100ms

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    GPIO.cleanup()  # Reset GPIO ports used in this script
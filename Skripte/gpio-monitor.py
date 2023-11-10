import RPi.GPIO as GPIO
import time
import keyboard

# Setting up GPIO
GPIO.setmode(GPIO.BCM)  # Use Broadcom SOC channel numbering
GPIO.setwarnings(False)

# List of GPIO ports you want to monitor
gpio_ports = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]

# Set up ports as input
for port in gpio_ports:
    GPIO.setup(port, GPIO.IN)

def print_gpio_status():
    print("GPIO Port Status")
    print("Port\tStatus")
    for port in gpio_ports:
        status = 'X' if GPIO.input(port) else ''
        print(f"{port}\t{status}")

try:
    while True:
        print_gpio_status()
        time.sleep(1)  # Refresh every 1 second
        if keyboard.is_pressed('x'):
            print("Exiting...")
            break

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    GPIO.cleanup()  # Reset GPIO ports used in this script

import RPi.GPIO as GPIO
import time
import sys

# Define your GPIO ports here
gpio_ports = [2, 3, 4, 17, 27, 22, 10, 9, 11, 5, 6, 13, 19, 26, 14, 15, 18, 23, 24, 25, 8, 7, 12, 16, 20, 21]

# Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
for port in gpio_ports:
    GPIO.setup(port, GPIO.IN)

# Function to process GPIO signal
def process_signal(port, status):
    if status:
        print(f"GPIO Signal Received on port {port}: High")
    else:
        print(f"GPIO Signal Received on port {port}: Low")

# Main function
def main():
    print("GPIO Monitoring started. Press CTRL+C to exit.")
    port_status = {port: GPIO.input(port) for port in gpio_ports}

    try:
        while True:
            for port in gpio_ports:
                current_status = GPIO.input(port)
                if current_status != port_status[port]:
                    process_signal(port, current_status)
                    port_status[port] = current_status
            time.sleep(0.1)  # Polling interval
    except KeyboardInterrupt:
        print("\nExiting...")
    finally:
        GPIO.cleanup()  # Reset GPIO ports on exit

if __name__ == "__main__":
    main()

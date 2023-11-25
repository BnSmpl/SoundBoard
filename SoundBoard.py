import sys
import tty
import termios
from soundDict import sounds

def getch():
    # Fetch a character from the stdin without requiring a newline
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

try:
    print("Program is running. Press 'q' to exit.")
    while True:
        char = getch()
        if char in sounds:
            print(f"Playing sound: {sounds[char]}")
        if char == 'q':  # Exit condition
            break
except KeyboardInterrupt:
    print("Exiting the program.")

print("Program exited.")

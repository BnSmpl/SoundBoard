import keyboard
import threading
import time


try:
    print("Program is running. Press Ctrl+C to exit.")
    while True:# main loop
        time.sleep(1) #remove when adding real code
        
except KeyboardInterrupt:
    print("Ctrl+C pressed. Exiting the program.")


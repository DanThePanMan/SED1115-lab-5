from machine import Pin
from utime import sleep


button = Pin(22, Pin.IN, Pin.PULL_DOWN)

while True:
    try:
        if button.value(): #if button is pressed
            print("pressed")
        while button.value(): #make it so one press sends once
            pass
    except KeyboardInterrupt:
        break
print("Finished.")

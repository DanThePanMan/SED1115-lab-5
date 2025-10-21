from machine import Pin
from machine import RTC


def log_event(message):
    try:
        with open("log.txt", "a") as f:
            f.write(str(message) + "\n")
            f.close()
    except Exception as e:
        print(f"Error writing to log: {e}")

button = Pin(22, Pin.IN, Pin.PULL_DOWN)

time_to_guess = 15

rtc = RTC()
rtc.datetime()
p15 = (rtc.datetime()[6] + time_to_guess) % 60


print("The game has started")
while True:
    

    try:
        if button.value(): #if button is pressed
            snapshot = rtc.datetime()[6] 
            

            diff = (p15 - snapshot) % 60
            
            if diff == 0:
                print("you got it")
            elif diff < 30:
            # pressed before target
                print(f"awe man, try again, you were {diff} seconds short")
                log_event(time_to_guess - diff)
            else:
                # pressed after target
                late_by = 60 - diff
                print(f"awe man, try again, you were {late_by} seconds too late")
                log_event(time_to_guess + late_by)
                rtc.datetime()
                
            # set up game again
            p15 = (rtc.datetime()[6] + time_to_guess) % 60


        while button.value(): #make it so one press sends once
            pass
    except KeyboardInterrupt:
        break
print("Finished.")

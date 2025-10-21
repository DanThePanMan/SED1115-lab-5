from machine import Pin
from machine import RTC

button = Pin(22, Pin.IN, Pin.PULL_DOWN)

time_to_guess = 15

rtc = RTC()
rtc.datetime()
p15 = rtc.datetime()[6] + time_to_guess
if p15 > 60:
    p15 = p15 - 60

print("The game has started")
while True:
    

    try:
        if button.value(): #if button is pressed
            if (rtc.datetime()[6] == p15):
                print("you got it")
            else:
                diff = p15 - rtc.datetime()[6] 
                
                if (rtc.datetime()[6] > p15):
                    diff = (rtc.datetime()[6] - p15)
                    print(f"awe man, try again, you were {diff} seconds too late")
                else:
                    print(f"awe man, try again, you were {diff} seconds short")

                rtc.datetime()
                p15 = rtc.datetime()[6] + time_to_guess
                if p15 > 60:
                    p15 = p15 - 60

        while button.value(): #make it so one press sends once
            pass
    except KeyboardInterrupt:
        break
print("Finished.")

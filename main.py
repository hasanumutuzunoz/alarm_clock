import sys
import datetime
import winsound
from threading import *
from keyboard import press


date_time = datetime.datetime.today()
print("Current Date : {}/{}/{}".format(date_time.day, date_time.month, date_time.year))
print("Current Time : {}:{}".format(date_time.hour, date_time.minute))
alarmHour = int(input("Enter alarm hour"))
alarmMinute = int(input("Enter alarm minute"))
alarmStop = False
musicFile = 'C:/Users/hasan/PycharmProjects/pythonMiniProjects/alarmClock/snowRabbit.wav'


def play():
    run_once = 1
    while True:
        # Update date time every second
        dt = datetime.datetime.today()

        # Start the alarm at alarm hour and alarm minute
        # Run this code once to prevent music error
        if run_once == 1 and dt.hour == alarmHour and dt.minute == alarmMinute:
            winsound.PlaySound(musicFile, winsound.SND_ASYNC)
            run_once = -1
            # Run the stop alarm thread at the same time.
            # This allows me to keep running this while loop while asking the user to stop the alarm.
            Thread(target=stop).start()

        # Stop the alarm after 1 minute, Stop thread 2
        elif dt.hour == alarmHour and dt.minute == alarmMinute + 1:
            winsound.PlaySound(None, winsound.SND_PURGE)
            # To stop thread 2, press enter while alarmStop True
            print("\nAlarm stopped after 1 minute")
            globals()["alarmStop"] = True
            press('enter')
            break

        # Stop thread 1 if thread 2 finished
        elif globals()["alarmStop"]:
            break


# Stop the music if input is 'STOP'
def stop():
    while not alarmStop:
        user_input_ref = str(input("To stop the alarm, type 'STOP'"))
        if user_input_ref == "STOP":
            winsound.PlaySound(None, winsound.SND_PURGE)
            globals()["alarmStop"] = True
            sys.exit()
        else:
            stop()


if __name__ == '__main__':
    Thread(target=play).start()


# Upcoming feature notes
"""
Add a snooze button (15min 5 min 10min options)
Choose days for the repeating alarm
"""

# I keep my previous versions here in comment for future reference
# V0
"""
# Play the sound in loop for 1 minute
while True:
    dt = datetime.datetime.today()
    if dt.hour == alarmHour and dt.minute == alarmMinute:
        alarmStarted = True
        print("Alarmmmm!!!!!")
        playsound(musicFile)
    elif alarmStarted:
        print("Alarm Stopped")
        break
"""
# V1
"""
# Play function
def play():
        if alarmStarted:
            winsound.PlaySound(musicFile, winsound.SND_ASYNC)
            #while True:
                #if not alarmStarted:
                 #   winsound.PlaySound(None, winsound.SND_PURGE)
                  #  break
            #time.sleep(5)
            #alarmStarted == False
            #winsound.PlaySound(None, winsound.SND_PURGE)
            #break
        #else:
            #winsound.PlaySound(None, winsound.SND_PURGE)
            #print("Alarm stopped")
            #break


def stop_input():
    while True:
        dt = datetime.datetime.today()
        if dt.hour == alarmHour and dt.minute == alarmMinute + 1:
            winsound.PlaySound(None, winsound.SND_PURGE)

        stop_alarm = str(input("To stop the alarm, type 'STOP'"))
        if stop_alarm == "STOP":
            alarmStarted = False
            winsound.PlaySound(None, winsound.SND_PURGE)
            break
        else:
            stop_input()
            

if __name__ == '__main__':
    start = play()
    stop = stop_input()

    Thread(target=start).start()
    Thread(target=stop).start()
"""
# V2
"""
class Start:
    def __init__(self):
        self.alarmStarted = False

    def run(self):

        # Play 1 minute
        run_once = 1
        while True:
            dt = datetime.datetime.today()
            if run_once == 1 and dt.hour == alarmHour and dt.minute == alarmMinute:
                self.alarmStarted = True
                print("alarmStarted {}".format(self.alarmStarted))
                winsound.PlaySound(musicFile, winsound.SND_ASYNC)
                run_once = -1

            elif dt.hour == alarmHour and dt.minute == alarmMinute + 1:
                winsound.PlaySound(None, winsound.SND_PURGE)
                sys.exit()
                break

            # Add else stopAlarm:
            # here


class Stop:
    def __init__(self, start):
        self.start = start

    def stop_button(self):
        while not self.start.alarmStarted:
            print("sleeping")
            time.sleep(1)

        if self.start.alarmStarted == True:
            print("asndoansdouansdoansd")
            stop_alarm = str(input("To stop the alarm, type 'STOP'"))
            if stop_alarm == "STOP":
                globals()["alarmStop"] = True
                winsound.PlaySound(None, winsound.SND_PURGE)
                sys.exit()
            self.start.c.release()
            
            
if __name__ == '__main__':
    start = Start()
    stop = Stop(start)

    Thread(target=start.run()).start()
    Thread(target=stop.stop_button()).start()
"""







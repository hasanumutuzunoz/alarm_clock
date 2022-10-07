import sys
import winsound
from datetime import datetime, timedelta, time
from threading import *
from keyboard import press


dt = datetime.now().replace(microsecond=0)
print("Current Date : {}/{}/{}".format(dt.day, dt.month, dt.year))
print("Current Time : {}:{}".format(dt.hour, dt.minute))
alarmHour, alarmMinute = [int(x) for x in input("Enter alarm hour and minute separated by : (e.g. 4:11) ").split(':')]
alarmTime = datetime(dt.year, dt.month, dt.day, alarmHour, alarmMinute, 0)
print("Alarm Time: ", alarmTime)
alarmStop = False
musicFile = 'C:/Users/hasan/PycharmProjects/pythonMiniProjects/alarmClock/snowRabbit.wav'
run_once = 1


def play():
    while True:
        # Update date time every second
        global dt, run_once, alarmTime
        dt = datetime.now().replace(microsecond=0)

        # Start the alarm at alarm hour and alarm minute
        # Run this code once to prevent music error
        if run_once == 1 and dt == alarmTime:
            winsound.PlaySound(musicFile, winsound.SND_ASYNC)
            run_once = -1
            # Run the stop alarm thread at the same time.
            # This allows me to keep running this while loop while asking the user to stop the alarm.
            Thread(target=stop).start()

        # Stop the alarm after 1 minute, Stop thread 2
        elif dt == alarmTime + timedelta(minutes=1):
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
    global dt, run_once, alarmTime, alarmStop
    while not alarmStop:
        user_input_ref = input("\nTo stop the alarm, type 'STOP'"
                               "\nTo snooze the alarm, enter minute ")
        # Snooze if the input is int
        if user_input_ref.strip().isdigit():
            winsound.PlaySound(None, winsound.SND_PURGE)
            user_input_ref = float(user_input_ref)
            alarmTime = dt + timedelta(minutes=user_input_ref)
            run_once = 1
            print("Alarm time: ", alarmTime)
            break

        # Stop if the input is 'STOP'
        elif user_input_ref == "STOP":
            winsound.PlaySound(None, winsound.SND_PURGE)
            globals()["alarmStop"] = True
            sys.exit()


if __name__ == '__main__':
    Thread(target=play).start()
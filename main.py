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









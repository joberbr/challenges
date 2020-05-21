import datetime
import time
from datetime import timedelta

print('Welcome to the Pomodoro timer.\nThe timer will start with 25 minutes.')
answer = input('Please enter "Y" to start Pomodoro timer.')

duration = timedelta(minutes=25)

if answer == 'Y':
    start_time = datetime.datetime.now()
    end_time = start_time + duration

    while (end_time - datetime.datetime.now()) > timedelta(seconds=0):
        print(str(end_time - datetime.datetime.now())[:7], end="\r")
        time.sleep(1)

    print('Time has ended! Good work!')
else:
    print('Thanks for playing')

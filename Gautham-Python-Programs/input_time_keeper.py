# find the time user takes to give the input
# calculate the time range by calculating the min input time and max input time,
# as the user may not be taking the same time to type his input every time to the millionth of a second
# create json with the min and max values

from timeit import time
from getpass import getpass
import json
import os


def input_time_keeper():
    start_time = time.time()
    pin = getpass("PIN: ")
    end_time = time.time()
    return createJson((end_time-start_time) * 0.5, (end_time-start_time) * 1.5) if not os.path.exists('time_taken.json') else readJson(end_time-start_time)


def createJson(min_time, max_time):
    with open('time_taken.json', 'w') as wf:
        json.dump({'min_time': min_time, 'max_time': max_time}, wf)
    return True if os.path.exists('time_taken.json') else False


def readJson(time_taken):
    with open('time_taken.json', 'r') as wf:
        time_taken_dict = json.load(wf)
    return time_taken_dict['min_time'] <= time_taken <= time_taken_dict['max_time']


print(input_time_keeper())

from timeit import time
from getpass import getpass

def input_time():
    start_time = time.time()
    pin = getpass()
    end_time = time.time()
    return end_time - start_time

print(input_time())
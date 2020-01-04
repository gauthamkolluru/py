import os
import time
from tkinter import messagebox
from tkinter import Tk


class TimeKeeper:
    def __init__(self, path_to_file=None):
        self.__greet_text = """Hello!
        Your Time & Todo Manager started running.

        It is advised to use these first 25 mins of your day in planning it!

        All the Best!

        Have a Great Day ahead!!!"""
        self.__title = "Time Keeper"
        self.__work_time = 1500
        self.__break_time = 300
        self.__work_time_text = "Good Job! Take a break"
        self.__break_time_text = "Back to Work!"
        self.__work_sessions_total = 16
        self.__work_session_count = 1

    def __greetings(self):
        root = Tk()
        root.withdraw()
        return messagebox.showinfo(self.__title, self.__greet_text)

    def start(self):
        self.__greetings()
        self.__sleep_time = self.__work_time
        root = Tk()
        root.withdraw()
        while self.__work_session_count <= self.__work_sessions_total:
            time.sleep(self.__sleep_time)
            if self.__sleep_time == self.__work_time:
                self.__work_session_count += 1
                messagebox.showinfo(self.__title, self.__work_time_text)
                if self.__work_session_count % 4:
                    self.__sleep_time = self.__break_time
                else:
                    self.__sleep_time = self.__break_time * 3
            else:
                messagebox.showinfo(self.__title, self.__break_time_text)
                self.__sleep_time = self.__work_time


if __name__ == "__main__":
    t = TimeKeeper()
    t.start()

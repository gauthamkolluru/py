import os
import time
from tkinter import messagebox
from tkinter import Tk
import subprocess
from datetime import datetime
from sys import exit


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
        self.__want_to_work_text = "Do you wish to work today?"
        os.makedirs(os.path.join(os.path.join(os.path.expanduser(
            '~'), 'Documents'), 'task_keeper'), exist_ok=True)
        self.__path_to_file = os.path.join(os.path.join(
            os.path.expanduser('~'), 'Documents'), 'task_keeper')
        self.__file_name = f"{datetime.now().strftime('%d%m%Y')}"
        self.__file_ext = ".md"
        self.__fully_qual_file_name = os.path.join(
            self.__path_to_file, (self.__file_name + self.__file_ext))
        self.__md_title = "title: Tasks & Notes\n"
        self.__md_author = "author: " + os.environ['USERNAME']+"\n"
        self.__md_date = f"date: {datetime.now().strftime('%B')} {datetime.now().strftime('%d')}, {datetime.now().strftime('%Y')}\n"
        self.__md_metadata_separator = "---\n"

    def __greetings(self):
        with open(self.__fully_qual_file_name, 'w') as fh:
            fh.writelines([self.__md_metadata_separator, self.__md_title, self.__md_author,
                           self.__md_date, self.__md_metadata_separator, "# Tasks & Notes\n\n", "## Tasks\n\n"])
        return messagebox.showinfo(self.__title, self.__greet_text)

    def __continue_dialog(self):
        return messagebox.askokcancel(self.__title, self.__want_to_work_text)

    def __file_calls(self):
        return subprocess.run(['start', self.__fully_qual_file_name], shell=True)

    def __time_keeper(self):
        self.__sleep_time = self.__work_time
        while self.__work_session_count <= self.__work_sessions_total:
            time.sleep(self.__sleep_time)
            if self.__sleep_time == self.__work_time:
                self.__work_session_count += 1
                messagebox.showinfo(self.__title, self.__work_time_text)
                self.__file_calls()
                if self.__work_session_count % 4:
                    self.__sleep_time = self.__break_time
                else:
                    self.__sleep_time = self.__break_time * 3
            else:
                messagebox.showinfo(self.__title, self.__break_time_text)
                self.__sleep_time = self.__work_time
        return 'ok'

    def start(self):
        root = Tk()
        root.withdraw()
        if self.__continue_dialog():
            if not os.path.exists(os.path.join(self.__path_to_file, (self.__file_name + self.__file_ext))):
                self.__greetings()
            self.__file_calls()
            self.__time_keeper()
        return exit(0)


if __name__ == "__main__":
    t = TimeKeeper()
    t.start()

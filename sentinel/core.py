import time
import os
import traceback

import psutil

from sentinel.exceptions import PsUtilError
from sentinel.utils.cron import add_to_crontab, EVEN_HOUR
from sentinel.utils.loader import Loader

ALLOWED_PROCESSES = [
    "postgres",
    "docker",
    "top",
    "netstat"
]


class ScriptGen:
    def __init__(self):
        self.allowed_list = ProcessTrie()
        add_to_crontab(EVEN_HOUR, os.path.abspath("scripts/basic_system_status.sh"))

    def scan(self, ):
        for proc in psutil.process_iter():
            try:
                p_info = proc.as_dict(attrs=['pid', 'name'])
                self.allowed_list.insert(p_info['name'])
            except Exception as e:
                traceback.print_exc()
                raise PsUtilError(e)
        return self

    def add_each(self):
        for process in ALLOWED_PROCESSES:
            if self.allowed_list.starts_with(process):
                if int(input(f"=> {process} detected. add?[1/0] :")):
                    with Loader(f"Installing {process} monitor..") as _:
                        time.sleep(2)


class ProcessTrie:
    def __init__(self):
        self.child = {}

    def insert(self, word):
        current = self.child
        for letter in word:
            if letter not in current:
                current[letter] = {}
            current = current[letter]
        current['#'] = 1

    def search(self, word):
        current = self.child
        for letter in word:
            if letter not in current:
                return False
            current = current[letter]
        return '#' in current

    def starts_with(self, prefix):
        current = self.child
        for letter in prefix:
            if letter not in current:
                return False
            current = current[letter]
        return True

import time
import os
import psutil

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
        self.allowed_list = set()
        add_to_crontab(EVEN_HOUR, os.path.abspath("scripts/basic_system_status.sh"))

    def scan(self, ):
        for proc in psutil.process_iter():
            try:
                p_info = proc.as_dict(attrs=['pid', 'name'])
                for process in ALLOWED_PROCESSES:
                    if p_info['name'].lower().startswith(process.strip().lower()):
                        self.put_allowed_list(p_info['name'].lower())
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return self

    def put_allowed_list(self, value):
        self.allowed_list.add(value)

    def add_each(self):
        for process in self.allowed_list:
            if int(input(f"=> {process} detected. add?[1/0] :")):
                with Loader(f"Installing {process} monitor..") as _:
                    time.sleep(2)

    def __str__(self):
        return " | ".join(self.allowed_list)

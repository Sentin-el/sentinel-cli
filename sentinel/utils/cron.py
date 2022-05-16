import os

EVEN_HOUR = "0 */2 * * *"


def add_to_crontab(schedule: str, script_path: str) -> None:
    os.system(f"(crontab -l ; echo \"{schedule} {script_path}\") 2>&1 | grep -v \"no crontab\" | sort | uniq | "
              f"crontab - ")

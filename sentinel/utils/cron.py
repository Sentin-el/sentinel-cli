import os

EVEN_HOUR = "0 */2 * * *"


def add_to_crontab(schedule: str, script_path: str) -> bool:
    os.system(f"(crontab -l ; echo \"{schedule} {script_path}\") 2>&1 | grep -v \"no crontab\" | sort | uniq | "
              f"crontab - ")
    return True


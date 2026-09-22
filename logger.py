import os
import platform
import psutil
import json

def main():
    search_data()


def search_data():
    comp_name = str(platform.node()) + str(os.getpid())
    logical_count = psutil.cpu_count(logical=True)
    used_memory = psutil.virtual_memory().used
    process_count = len(psutil.pids())
    thread_count = 0
    for process in psutil.process_iter():
        try:
            thread_count += process.num_threads()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    cpu_load = psutil.cpu_percent(interval=1)
    disk_usage = psutil.disk_usage(os.path.abspath(os.sep)).used
    cpu_speed = psutil.cpu_freq().current

    data = {
        "Имя Компа": comp_name,
        "Логические процессы": logical_count,
        "Использованно памяти": used_memory,
        "Число процессов": process_count,
        "Число потоков": thread_count,
        "Загрузка процессора": cpu_load,
        "Занято памяти на диске": disk_usage,
        "Скорость процессора": cpu_speed
    }

    save_data(data)

def save_data(data: dict):
    name = "data.json"

    with open(name, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

main()

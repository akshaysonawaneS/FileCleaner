import time
from os.path import expanduser
from watchdog.observers import Observer
from main import Cleaner
from sys import platform

if __name__ == "__main__":
    if platform == "linux" or platform == "macOS":
        check_path = expanduser("~") + "/Downloads/"
    elif platform == "windows":
        check_path = expanduser("~") + r"\Downloads\\"

    event_handler = Cleaner(check_path)
    observer = Observer()
    observer.schedule(event_handler, path=check_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

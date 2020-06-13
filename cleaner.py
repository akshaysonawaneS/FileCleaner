import time
from os.path import expanduser
from watchdog.observers import Observer
from main import Cleaner

if __name__ == "__main__":
    check_path = expanduser("~") + "/Downloads"

    event_handler = Cleaner(check_path)
    observer = Observer()
    observer.schedule(event_handler, path=check_path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

from watchdog.events import FileSystemEventHandler
from os import listdir
from os.path import isfile

class Cleaner(FileSystemEventHandler):
    def __init__(self, check_path):
        self.check_path = check_path

    def on_modified(self, event):
        for file in listdir(self.check_path):
            if isfile(self.check_path + "/" +file):
                print(file)
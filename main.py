from watchdog.events import FileSystemEventHandler
from os import listdir, mkdir, rename
from os.path import isfile, exists, splitext
from sys import platform
from Extension import all_extension, all_extension_windows
import shutil

def rename_file(filename, file_extension, check_path, path):
    """
    Renaming the file it already exists in destination folder
    :param filename: file name
    :param file_extension: file extension
    :return: new file name
    """
    i = 0
    new_name = filename + file_extension
    while exists(path  + new_name):
        i = i + 1
        new_name = filename + str(i) + file_extension
    rename(check_path + filename + file_extension, check_path  + new_name)

    return new_name


def move_file(check_path, file):
    """
    Moving file downloaded to specific folder
    :param path: file path
    :param file: file name
    :return: Null
    """
    filename, file_extension = splitext(file)
    if file_extension in all_extension:
        if exists(check_path + all_extension[file_extension] + file):
            file = rename_file(filename, file_extension, check_path, check_path + all_extension[file_extension])
        else:
            shutil.move(check_path + file, check_path + all_extension[file_extension])
    elif file_extension not in all_extension:
        if exists(check_path + "/Others/" + file):
            file = rename_file(filename, file_extension,check_path, check_path+"Others/")
            shutil.move(check_path + file, check_path + "Others")
        else:
            shutil.move(check_path  + file, check_path + "Others")


def initializeFolders(path):
    """
    Initialize destination path with important folder by categoery
    :return: Null
    """
    my_folders = ["Videos", "Images", "Others", "PDFs", "TxtFiles", "Microsoft", "ZipFiles", "Audio", "Executable"]
    present_folders = listdir(path)
    for folder in my_folders:
        if folder not in present_folders:
            mkdir(path + folder)


class Cleaner(FileSystemEventHandler):
    def __init__(self, check_path):
        self.check_path = check_path
        initializeFolders(self.check_path)

    def on_modified(self, event):
        for file in listdir(self.check_path):
            if platform == "linux" or platform == "macOS":
                if isfile(self.check_path +file):
                    move_file(self.check_path,file)
            elif platform == "windows":
                pass

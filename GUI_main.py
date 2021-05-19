import os
import time
import json
import threading
from pathlib import Path
from difflib import SequenceMatcher
import PySimpleGUI as sg
import subprocess as sp
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

current_dir = os.getcwd()
layout = [
    [sg.Text(current_dir)], 
    [sg.Button("Auto"), sg.Button("Manual")],
    [sg.Button("Open file")],
    [sg.Text("Dir/File status:"), sg.Text("NULL", key="_STAT_")],
]
window = sg.Window("Filer", layout)        

while True:
    target, values = window.read()
    if target == sg.WIN_CLOSED:
        break
    elif target == "Auto":
        sg.popup("The Process is starting.")
        list_of_files = []
        folder_list = []
        list_numbers = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
        class CatFiles:
            def __init__(self):
                self.observer = Observer()
            def run(self):
                event_handler = CatHandler()
                self.observer.schedule(event_handler, current_dir, recursive=True)
                self.observer.start()
                
                try:
                    while True:
                        time.sleep(10)
                except:
                    self.observer.stop()
                    print("observer stopping...")
                self.observer.join()
        
        class CatHandler(FileSystemEventHandler):
            def on_any_event(self, event):
                print(type(event))
                if event.is_directory:
                    return None
                elif event.event_type == "created":
                    print("creatded")
                elif event.event_type == "modified":
                    print("modded")
                    new_file = event.src_path
                    for i in list_numbers:
                        updated = new_file.split("\\")
                        dir_length = len(updated)
                        if i == dir_length:
                            L_filename = updated[i - 1]
                            final_filename = L_filename.split(".")[0]
                    print(final_filename, " <-- modified file")
                    print("folders: ")
                    for folders in os.listdir():
                        if os.path.isdir(os.path.join(folders)):
                            matcher = SequenceMatcher(None, folders, final_filename).ratio()
                            list_of_files.append(matcher)
                            folder_list.append(folders)
                            maximum = max(list_of_files)
                            print(maximum)
                            max_index = list_of_files.index(maximum)
                            print(max_index)
                  
                    for scan in os.scandir():
                        if scan.is_dir():
                            continue
                        file_path = str(Path(scan))
                        if L_filename == file_path:
                            current_fp = Path(scan)
                            combine_path = "{}\\{}\\{}".format(current_dir, folder_list[max_index], current_fp)
                            print(combine_path)
                            dir_path = Path(current_dir)
                            path = current_fp.rename(dir_path.joinpath(combine_path))
                            print(path)
                            print("sent to {}".format(folder_list[max_index]))
                else:
                    print("nothin")
                       
                
        if __name__ == "__main__":
            watch = CatFiles()
            watch.run()

    #underdeveloped
    elif target == "Open file":
        for scan in os.scandir():
            if scan.is_dir():
                continue
            file_path = str(Path(scan))
            
            f_format = file_path.split(".")[1]
            #i know theres more i just dont want to lkist them all
            #photoshop opening is coming out soon
            notepad_list = [".txt", ".py", ".js", ".r", ".java", ".cpp", ".c", ".h", ".i", ".pyw", ".go", ".ts", ".tsx"]
            for i in notepad_list:
                file_paths = Path(scan)
                if file_paths.is_dir():
                    program_open = "notepad.exe"
                    file_dir = "{}\\{}".format(current_dir, file_paths)
                    print(file_dir)
        sp.Popen([program_open, file_dir])


window.close()                                                                                          
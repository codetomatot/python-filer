import os
import json
import threading
from pathlib import Path
import PySimpleGUI as sg
import subprocess as sp


current_dir = os.getcwd()
layout = [
    [sg.Text(current_dir)], 
    [sg.Button("Auto"), sg.Button("Manual")],
    [sg.Button("Open file")],
    [sg.Text("Dir/File status:"), sg.Text("NULL", key="_STAT_")],
    [sg.Input()],
]
window = sg.Window("Filer", layout) 

def watch_func():
    import main

def gui_thread():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Auto":
            param = None
            sg.popup("The Process is starting.")
            try:
                threading.Thread(target=watch_func).start()
            except Exception as e:
                print(e)
                print("Wonts start")
        elif event == "Open file":
            file_name = sg.popup_get_text(message="Enter file name that exists in curent directrory\n{}".format(current_dir),
                title=None,
                default_text="",
                password_char="",
                size = (None, None),
                button_color = None,
                background_color = None,
                text_color = None,
                icon = None,
                font = None,
                no_titlebar = False,
                grab_anywhere = False,
                keep_on_top = False,
                location = (None, None),
                image = None,
                modal = True
            )
            # print(file_name)
            for scan in os.scandir():
                if scan.is_dir():
                    continue
                file_path = str(Path(scan))
                
                f_format = file_path.split(".")[1]
                
                notepad_list = [".txt", ".py", ".js", ".r", ".java", ".cpp", ".c", ".h", ".i", ".pyw", ".go", ".ts", ".tsx"]
                for i in notepad_list:
                    file_paths = Path(scan)
                    if f_format == ".psd" or f_format == ".ps":
                        program_to_open = "photoshop.exe"
                    else:
                        program_to_open = "notepad.exe"
            sp.Popen([program_to_open, "{}\\{}".format(current_dir, file_name)])

if __name__ == "__main__":
    try:
        gui_thread()
    except KeyboardInterrupt:
        print("Exiting")

window.close()                                                                                          
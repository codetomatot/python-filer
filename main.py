import os
from pathlib import Path
from difflib import SequenceMatcher

class CatFiles:
    def __init__(self, file_name, file_format):
        self.file_name = file_name
        self.file_format = file_format
inputs_amount = int(input("How many files: "))
def main(inputs):
    if inputs > 0:
        for i in range(1, inputs + 1):
            file_input = str(input("Enter file name: "))
            file_in_folder = False
            list_of_files = []
            folder_list = []

            file1 = CatFiles(file_input, " ")

            for folder_name in os.listdir():
                if os.path.isdir(os.path.join(folder_name)):
                    matcher = SequenceMatcher(None, folder_name, file_input).ratio()
                    folder_list.append(folder_name)
                    list_of_files.append(matcher)
                    maximum = max(list_of_files)
                    max_index = list_of_files.index(maximum)
                    print(folder_name, " <-- folders")
        

            for scan in os.scandir():
                if scan.is_dir():
                    continue
                file_path = str(Path(scan))
                print(file_path)
                print(file_input)
                current_path = os.getcwd()
                print(type(current_path))
            
                if file_input == file_path: #try "in" insead of "=="
                    file_path = Path(scan)
                    print(file_path, " <-- new scan file_path")
                    print("truuuee")
                    #dir_path = file_path.absolute()
                    combine_path = "{}\\{}\\{}".format(current_path, folder_list[max_index], file_path)
                    #print(combine_path)
                    dir_path = Path(current_path)
                    path = file_path.rename(dir_path.joinpath(combine_path))
                    print(path)
                    #.joinpath(f"images\\{file_path}".format())
                else:
                    print("false")
                    print(file_path, " <-- this is file_path")
                    print(current_path)
                    print(" ")
    print(max_index)
    print(folder_list[max_index])
    print(folder_list)
    print(" ")
    print(maximum)

main(inputs_amount)



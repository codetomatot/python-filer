# python-filer
What this will do is scan your current directory and wait until a file is created or modded to make changes to the directory. When a file is modified it will look for a folder in the already specified directory and compare the folders name to the files name and depending on how close the ratio and which ratio is largest out of all the other folders, it will send the file into the folder with the best fit/ biggest ratio.

also comes with a GUI and uses threading to make it as fast as possible.

import os
import sys

base = "Data"


def get_folders():
    tmp = []
    for dir, folder, files in os.walk(base):
        try:
            if len(folder) != 0 and sys.argv[1] in dir.lower():
                tmp.append(f"{dir}/{folder}")
        except IndexError as e:
            get_help(e)
            exit()
    return tmp

def get_help(error):
    if IndexError:
        print("Missing parameter python3 main.py [FOLDER]")
    

def main():
    
    requested_folders = get_folders()

    print(requested_folders)


main()

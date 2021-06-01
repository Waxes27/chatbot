import os
import sys

base = "Data"


def get_folders():
    tmp = []
    for dir, folder, files in os.walk(base):
        if len(folder) != 0 and sys.argv[1] in dir.lower():
            tmp.append(f"{dir}/{folder}")
    return tmp

def main():
    
    requested_folders = get_folders()

    print(requested_folders)


main()

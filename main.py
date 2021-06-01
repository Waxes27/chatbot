import os

base = "Data"


def get_folders():
    for dir, folder, files in os.walk(base):
        if len(folder) != 0:
            print(f"{dir}/{folder}")


def main():
    get_folders()


main()

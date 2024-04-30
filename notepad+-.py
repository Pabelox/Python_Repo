import os
import subprocess

class OpenFile:
    @staticmethod
    def road():
        return input("Podaj ścieżkę do pliku: ")

    @staticmethod
    def plik(file):
        with open(file) as f:
            return f.read()

    @staticmethod
    #do zastąpienia przez własny edytor w tk
    def edycja(note_file):
        subprocess.Popen(['ls'])

def edit_file():
    try:
        file_path = OpenFile.road()
        user_input_open = OpenFile.plik(file_path)
        print("Otwarto plik:", file_path)
        print("Zawartość pliku:")
        print(user_input_open)
        OpenFile.edycja(file_path)

    except Exception as e:
        print("Wystąpił błąd:", e)

if __name__ == '__main__':
    edit_file()

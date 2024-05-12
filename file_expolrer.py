import os
import subprocess

class OpenFile:


    @staticmethod
    def plik(file):
        os.listdir(file)



        

if __name__ == '__main__':
    innn = input("Podaj ścieżkę do pliku: ")

    print(OpenFile.plik(f'{innn}'))
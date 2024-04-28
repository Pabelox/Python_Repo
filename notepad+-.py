import os
def otwieranie():
    user_file = input("Podaj scierzkę do pliku")
    textfile = open(user_file)

    print(bool(textfile))

if __name__ == '__main__':
    otwieranie()
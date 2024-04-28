import os

class OpenFile:
    def road(rd):
        return os.path.abspath(rd)

    def plik(file):
        x = open(file)
        return x.read()





def edit_file():
    user_file = input("Podaj scierzkę do pliku")

    try:
        user_input_open = OpenFile.plik(user_file)

        if bool(user_input_open) == True:

            print(OpenFile.road(user_file))
            print(OpenFile.plik(user_file))



    except:
        print("Ściszka do pliku jest błędna")




if __name__ == '__main__':
    edit_file()



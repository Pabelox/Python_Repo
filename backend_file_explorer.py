import os
def files_list(file):
    if os.path.exists(file) == True:
        slfl = {}
        ids = 0
        for items in os.listdir(file):
            slfl.update({ids: f"{items}"})
            ids += 1
        return slfl
    else:
        return print("Ścierzka niepoprawna")

class InputsMethod:
    @staticmethod
    #zmiana aktualnego katalogu i zwrot aktualenej ścieszki
    def catalog_change(file_patch):
        if os.path.exists(file_patch) == True:
            (file_patch)
            return print(os.getcwd())
        else:
            return print("Ścierzka niepoprawna")
    @staticmethod
    #Lista aktualnego folderu
    def current():
        return os.listdir(os.getcwd())
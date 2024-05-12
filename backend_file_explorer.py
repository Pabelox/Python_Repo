import os


class InputsMethod:
    @staticmethod
    def files_list(file):                               #lista folderów i plików  w bierzącym folderze
        if os.path.exists(file) == True:                #sprawdzmy czy ścierzka istnieje
            return os.listdir(file)
        else:
            return print("Ścierzka niepoprawna")
    @staticmethod
    def catalog_change(file_patch):
        if os.path.exists(file_patch) == True:
            os.chdir(file_patch)
            return print(os.getcwd())
        else:
            return print("Ścierzka niepoprawna")
    @staticmethod
    def current():
        for w in os.listdir(os.getcwd()):
            print("->",w)
            return os.listdir(os.getcwd())


    @staticmethod
    def mover(lista :list) -> dict:
            slfl = {}
            ids = 0
            for items in lista:
                slfl.update({ids :f"{items}"})
                ids +=1
            print(slfl)

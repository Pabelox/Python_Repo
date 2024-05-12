import os
import subprocess
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
    def current_list():
        return os.listdir(os.getcwd())
    @staticmethod
    def current():
        return os.getcwd()


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
def move(insert_patch):
            fl = files_list(insert_patch).items()
            klucze = files_list(insert_patch).keys()
            for w ,z  in fl:
                print(w,z)

            nex = input("Wybierz folder pod który chcesz przejść")
            itnx  =int(nex)
            print(files_list(insert_patch)[itnx])
            for ks in klucze:
                if ks == itnx:
                    patch = files_list(insert_patch)[ks]
                    index = patch.find(".")
                    if index == -1:
                        os.chdir(os.path.join(insert_patch, patch))
                    else:
                        subprocess.run(["start", os.path.join(insert_patch, patch)], shell=True)

                        break



from backend_file_explorer import InputsMethod as IM
import backend_file_explorer as be
import os


if __name__ == '__main__':
    while True :

        chopt = input("\nWybierz opcje:\n"
                            "1: Start Explore \n"
                            "2: Zmień obecny folder\n"
                            "3: Obecny folder\n"
                            "exit to Exit\n"
                            "Opcja: ")

        if chopt == "1":
            inp1 = input("Podaj ścierzkę: ")

            print("Lista folderu: \n")
            flslst = be.files_list(inp1).items()
            klucze = be.files_list(inp1).keys()
            for w ,z  in flslst:
                print(w,z)

            nex = input("Wybierz folder pod który chcesz przejść")
            itnx  =int(nex)
            print(be.files_list(inp1)[itnx])
            for ks in  klucze :
                if ks == itnx:
                    os.chdir(f"{inp1}/{be.files_list(inp1)[ks]}")
                    break








        elif chopt == "2":
            inp2 = input("Podaj ścierzkę")
            IM.catalog_change(inp2)
            continue
        elif chopt == "3":
            for w in IM.current():
                print(w)
        elif chopt == "exit":
            print("Exit processing")
            break
        else:
            print("wybrano błędną opcję")
            continue





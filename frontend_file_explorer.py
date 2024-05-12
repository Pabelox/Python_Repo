from backend_file_explorer import InputsMethod as IM

if __name__ == '__main__':
    while True :




        chopt = input("\nWybierz opcje:\n"
                            "1: Wypisz zawartość podanego folderu \n"
                            "2: Zmień obecny folder\n"
                            "3: Obecny folder\n"
                            "9: Exit\n"
                            "Opcja: ")

        if chopt == "1":
            inp1 = input("Podaj ścierzkę: ")
            for w in IM.files_list(inp1):
                print(w)
            continue
        elif chopt == "2":
            inp2 = input("Podaj ścierzkę")
            IM.catalog_change(inp2)
            continue
        elif chopt == "3":
            IM.current()
        elif chopt == "9":
            print("Exit processing")
            break
        else:
            print("wybrano błędną opcję")
            continue





from backend_file_explorer import InputsMethod as IM
import backend_file_explorer as be
import os


if __name__ == '__main__':
    while True :

        chopt = input("\nWybierz opcje:\n"
                            "1: Przejdź pod inny folder wybrany z listy \n"
                            "2: Zmień obecny folder\n"
                            "3: Przejdz pod inny folder w ramach obecnego\n"
                            "4: Obecny folder\n"
                            "exit to Exit\n"
                            "Opcja: ")

        if chopt == "1":
            inp1 = input("Podaj ścierzkę: ")
            be.move(inp1)
        elif chopt == "2":
            inp2 = input("Podaj ścierzkę")
            IM.catalog_change(inp2)
            continue
        elif chopt == "3":
            be.move(IM.current())
        elif chopt == "4":
            for w in IM.current_list():
                print(w)
        elif chopt == "exit":
            print("Exit processing")
            break
        else:
            print("wybrano błędną opcję")
            continue





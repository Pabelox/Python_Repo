
string = ".121e1e"

index = string.find(".")
if index == 0:
    print(f"Znaleziono kropkę na pozycji {index}.")
elif index == -1:
    print(-1)
else:
    print("Nie znaleziono kropki.")

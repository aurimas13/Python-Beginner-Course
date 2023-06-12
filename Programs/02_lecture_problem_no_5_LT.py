metai = int(input("Įveskite metus: "))

if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
    print("Keliamieji metai")
else:
    print("Nekeliamieji metai")

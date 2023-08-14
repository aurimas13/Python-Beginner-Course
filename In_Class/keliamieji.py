def ar_keliamieji(metai):
    if (metai % 400 == 0) or (metai % 4 == 0 and metai % 100 != 0):
        return("Keliamieji")
    else:
        return("Nekeliamieji")

if __name__ == "__main__":
    print(ar_keliamieji(2000))
    print(ar_keliamieji(2020))
    print(ar_keliamieji(2100))

#Keliamieji
#Keliamieji
#Nekeliamieji
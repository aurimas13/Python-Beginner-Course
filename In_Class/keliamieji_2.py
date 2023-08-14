def ar_keliamieji(metai):
    if (metai % 400 == 0) or (metai % 4 == 0):
        return("Keliamieji")
    else:
        return("Nekeliamieji")

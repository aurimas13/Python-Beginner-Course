for metai in range(1900, 2101):
    if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 == 0):
        print(metai)

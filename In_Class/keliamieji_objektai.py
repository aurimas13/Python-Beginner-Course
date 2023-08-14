class Keliamieji:

    def tikrinti(self, metai):
        return (metai % 400 == 0) or (metai % 4 == 0 and metai % 100 != 0)

    def diapazonas(self, nuo, iki):
        sarasas = []
        for metai in range(nuo, iki):
            if (metai % 400 == 0) or (metai % 4 == 0 and metai % 100 != 0):
                sarasas.append(metai)
            # if Keliamieji.tikrinti(metai):
            #     sarasas.append(metai)
        return sarasas

#Keliamieji
#Keliamieji
#Nekeliamieji
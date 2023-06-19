# Atspausdinti, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių:
def skaciuoti_simbolius(string):
    zodziai = string.split() # "As esu Aurimas"
    num_zodziai = len(zodziai)
    num_didziosios = sum(1 for raide in string if raide.isupper())
    num_mazosios = sum(1 for raide in string if raide.islower())
    suma = 0
    for raide in string:
        if raide.islower():
            suma += 1
    num_skaiciai = sum(1 for skaicius in string if skaicius.isdigit() )

    print("Žodžių skaičius:", num_zodziai)
    print("Didžiųjų raidžių skaičius:", num_didziosios)
    print("Mažųjų raidžių skaičius:", num_mazosios)
    print("Mažųjų raidžių skaičius:", suma)
    print("Skaičių skaičius:", num_skaiciai)

    # return num_zodziai, num_didziosios, num_mazosios, num_skaiciai

if __name__ == '__main__':
    print(skaciuoti_simbolius("As esu Aurimas"))
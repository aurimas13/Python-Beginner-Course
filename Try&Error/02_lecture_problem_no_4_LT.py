import random

# Ciklas, kuris sugeneruoja tris atsitiktinius skaičius
while True:
    # Sugeneruojame tris atsitiktinius skaičius nuo 1 iki 6
    skaicius1 = random.randint(1, 6)
    skaicius2 = random.randint(1, 6)
    skaicius3 = random.randint(1, 6)
    
    # Tikriname, ar bent vienas iš skaičių yra 5
    if skaicius1 == 5 or skaicius2 == 5 or skaicius3 == 5:
        # Jei taip, atspausdiname pranešimą ir nutraukiame ciklą
        print("Pralaimėjai...")
        break
    else:
        # Jei ne, atspausdiname pranešimą ir nutraukiame ciklą
        print("Laimėjai!")
        break

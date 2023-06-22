# Kintamasis, kuriame laikysime teigiamų skaičių sumą
teigiamu_suma = 0

# Besikartojantis ciklas, kuris leis vartotojui įvesti skaičius
while True:
    # Paprašome vartotojo įvesti skaičių
    skaicius = float(input("Įveskite skaičių: "))
    
    # Tikriname ar įvestas skaičius yra teigiamas
    if skaicius > 0:
        # Pridedame teigiamą skaičių prie sumos
        teigiamu_suma += skaicius
    else:
        # Jei skaičius neigiamas, nutraukiame ciklą
        break

# Atspausdiname visų įvestų teigiamų skaičių sumą
print(f"Visų įvestų teigiamų skaičių suma yra {teigiamu_suma}")

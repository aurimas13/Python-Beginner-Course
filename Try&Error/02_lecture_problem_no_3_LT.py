# Sukuriamas sąrašas, kuriame bus saugomi žodžiai
zodziu_sarasas = []

# Paprašome vartotojo įvesti, kiek žodžių jis nori pridėti
kiekis = int(input("Įveskite, kiek žodžių norite pridėti: "))

# Ciklas, kuris leidžia vartotojui įvesti nurodytą žodžių kiekį
for i in range(kiekis):
    # Paprašome vartotojo įvesti žodį
    zodis = input(f"Įveskite {i + 1}-ąjį žodį: ")
    # Pridedame žodį į sąrašą
    zodziu_sarasas.append(zodis)

# Ciklas, kuris peržiūri kiekvieną žodį sąraše ir atspausdina jį, jo ilgį ir eilės numerį
for zodis in zodziu_sarasas:
    # Gauname žodžio ilgį
    ilgis = len(zodis)
    # Gauname žodžio eilės numerį sąraše
    eiles_numeris = zodziu_sarasas.index(zodis) + 1
    # Atspausdiname informac

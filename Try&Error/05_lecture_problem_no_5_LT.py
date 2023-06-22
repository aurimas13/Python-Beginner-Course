# Ši klasė atstovauja vieną pajamų ar išlaidų įrašą
class Irasas:
    def __init__(self, tipas, suma):
        # Inicijuojame įrašą su jo tipu (pajamos arba išlaidos) ir suma
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        # Apsibrėžiame, kaip konvertuoti įrašą į eilutę, kuri bus naudojama spausdinant įrašą
        return f"{self.tipas}: {self.suma}"

# Ši klasė atstovauja biudžetą, kuriame yra daugybė pajamų ir išlaidų įrašų
class Biudzetas:
    def __init__(self):
        # Inicijuojame biudžetą su tuščiu įrašų sąrašu
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        # Pridedame pajamų įrašą į biudžetą
        self.zurnalas.append(Irasas("Pajamos", suma))

    def prideti_islaidu_irasa(self, suma):
        # Pridedame išlaidų įrašą į biudžetą, išlaidas atstovaujant neigiamomis sumomis
        self.zurnalas.append(Irasas("Islaidos", -suma))

    def gauti_balansa(self):
        # Apskaičiuojame ir grąžiname biudžeto balansą, kuris yra visų įrašų sumų suma
        return sum(irasa.suma for irasa in self.zurnalas)

    def parodyti_ataskaita(self):
        # Spausdiname visus biudžeto įrašus
        for irasas in self.zurnalas:
            print(irasas)

# Sukurkite biudžetą
biudzetas = Biudzetas()

# Pradėkite ciklą, kuris bus vykdomas, kol vartotojas pasirenka išjungti programą
while True:
    # Spausdiname parinktis, iš kurių vartotojas gali pasirinkti
    print("1. Įvesti pajamas")
    print("2. Įvesti išlaidas")
    print("3. Parodyti balansą")
    print("4. Parodyti ataskaitą")
    print("5. Išeiti iš programos")

    # Paprašome vartotojo pasirinkti parinktį
    choice = input("Pasirinkite veiksmą: ")

    # Tikriname, kurią parinktį pasirinko vartotojas, ir atliekame atitinkamą veiksmą
    if choice == "1":
        # Paprašome vartotojo įvesti pajamų sumą,```python
        # tada pridedame ją prie biudžeto
        suma = float(input("Įveskite pajamų sumą: "))
        biudzetas.prideti_pajamu_irasa(suma)
    elif choice == "2":
        # Paprašome vartotojo įvesti išlaidų sumą, tada pridedame ją prie biudžeto
        suma = float(input("Įveskite išlaidų sumą: "))
        biudzetas.prideti_islaidu_irasa(suma)
    elif choice == "3":
        # Spausdiname dabartinį biudžeto balansą
        print(f"Balansas: {biudzetas.gauti_balansa()}")
    elif choice == "4":
        # Spausdiname visų pajamų ir išlaidų įrašų biudžeto ataskaitą
        biudzetas.parodyti_ataskaita()
    elif choice == "5":
        # Išeiname iš programos
        break
    else:
        # Jei vartotojas įvedė kažką kitą nei 1-5, spausdiname klaidos pranešimą
        print("Netinkamas pasirinkimas. Bandykite dar kartą.")

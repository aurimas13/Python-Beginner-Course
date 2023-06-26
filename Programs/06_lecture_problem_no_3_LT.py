# Sukuriame tėvinę klasę Įrašas su savybe suma
class Irasas:
    def __init__(self, suma):
        self.suma = suma  # Priskiriamas sumos kintamasis

# Sukuriame klasę Pajamų Įrašas, kuri paveldi savybes iš tėvinės klasės Įrašas
class PajamuIrasas(Irasas):
    def __init__(self, suma, siuntejas, papildoma_informacija):
        super().__init__(suma)  # Naudojame super(), kad priskirtume sumą iš tėvinės klasės
        self.siuntejas = siuntejas  # Priskiriamas siuntėjo kintamasis
        self.papildoma_informacija = papildoma_informacija  # Priskiriama papildoma informacija

# Sukuriame klasę Išlaidų Įrašas, kuri paveldi savybes iš tėvinės klasės Įrašas
class IslaiduIrasas(Irasas):
    def __init__(self, suma, atsiskaitymo_budas, isigyta_preke_paslauga):
        super().__init__(suma)  # Naudojame super(), kad priskirtume sumą iš tėvinės klasės
        self.atsiskaitymo_budas = atsiskaitymo_budas  # Priskiriamas atsiskaitymo būdas
        self.isigyta_preke_paslauga = isigyta_preke_paslauga  # Priskiriama įsigyta prekė ar paslauga

# Sukuriame klasę Biudžetas
class Biudzetas:
    def __init__(self):
        self.zurnalas = []  # Priskiriamas tuščias sąrašas žurnalui

    # Funkcija, leidžianti pridėti įrašą į žurnalą
    def prideti_irasa(self, irasas):
        self.zurnalas.append(irasas)  # Įrašas pridedamas į žurnalą

    # Funkcija, leidžianti gauti balansą
    def gauti_balansa(self):
        balansas = 0  # Pradinis balansas nustatomas 0
        # Iteruojame per visus įrašus žurnale
        for irasas in self.zurnalas:
            # Tikriname, ar įrašas yra pajamų įrašas
            if isinstance(irasas, PajamuIrasas):
                balansas += irasas.suma  # Jei taip, pridedame sumą prie balanso
            # Tikriname, ar įrašas yra išlaidų įrašas
            elif isinstance(irasas, IslaiduIrasas):
                balansas -= irasas.suma  # Jei taip, atimame sumą iš balanso
        return balansas  # Grąžiname galutinį balansą

    # Funkcija, leidžianti gauti ataskaitą
    def gauti_ataskaita(self):
        # Iteruojame per visus įrašus žurnale
        for irasas in self.zurnalas:
            # Tikriname, ar įrašas yra pajamų įrašas
            if isinstance(irasas, PajamuIrasas):
                # Jei taip, spausdiname visą informaciją apie pajamų įrašą
                print(f"Pajamos: {irasas.suma}, Siuntėjas: {irasas.siuntejas}, Papildoma informacija: {irasas.papildoma_informacija}")
            # Tikriname, ar įrašas yra išlaidų įrašas
            elif isinstance(irasas, IslaiduIrasas):
                # Jei taip, spausdiname visą informaciją apie išlaidų įrašą
                print(f"Išlaidos: {irasas.suma}, Atsiskaitymo būdas: {irasas.atsiskaitymo_budas}, Įsigyta prekė/paslauga: {irasas.isigyta_preke_paslauga}")

# Testavimas
biudzetas = Biudzetas()  # Sukuriamas biudžeto objektas
# Pridedamas pajamų įrašas į biudžetą
biudzetas.prideti_irasa(PajamuIrasas(500, "Jonas", "Atlyginimas"))
# Pridedamas išlaidų įrašas į biudžetą
biudzetas.prideti_irasa(IslaiduIrasas(200, "Grynaisiais", "Maistas"))
biudzetas.gauti_ataskaita()  # Spausdinama ataskaita
# Spausdinamas galutinis balansas
print(f"Balansas: {biudzetas.gauti_balansa()}")

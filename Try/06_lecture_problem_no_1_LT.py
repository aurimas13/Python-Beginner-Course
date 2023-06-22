class Automobilis:
    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        # Atspausdinama automobilio informacija sukūrus objektą
        print(f"Automobilis: Metai - {self.metai}, Modelis - {self.modelis}, Kuro tipas - {self.kuro_tipas}")

    def vaziuoti(self):
        print("Važiuoja")

    def stoveti(self):
        print("Priparkuota")

    def pildyti_degalu(self):
        print("Degalai įpilti")


class Elektromobilis(Automobilis):
    def __init__(self, metai, modelis):
        # Elektromobilio kuro tipas visada yra elektra
        super().__init__(metai, modelis, "elektra")

    # Perrašomas pildyti_degalu metodas
    def pildyti_degalu(self):
        print("Baterija įkrauta")

    # Pridedamas vaziuoti_autonomiskai metodas
    def vaziuoti_autonomiskai(self):
        print("Važiuoja autonomiškai")


# Sukuriamas Automobilio objektas
auto = Automobilis(2022, "BMW", "benzinas")

# Sukuriamas Elektromobilio objektas
elektro_auto = Elektromobilis(2023, "Tesla")

# Su Automobilio objektu paleidžiamos funkcijos
auto.vaziuoti()
auto.stoveti()
auto.pildyti_degalu()

# Su Elektromobilio objektu paleidžiamos funkcijos
elektro_auto.vaziuoti()
elektro_auto.stoveti()
elektro_auto.pildyti_degalu()
elektro_auto.vaziuoti_autonomiskai()

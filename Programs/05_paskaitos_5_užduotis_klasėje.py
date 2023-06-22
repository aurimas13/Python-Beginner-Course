# Sukursime klase kuri atovauja viena pajamu ir islaidu irasa
class Irasas:
    # Inicijuosime irasa su jo tipu (pajamos abra islaidos) ir suma
    def __init__(self, tipas, suma):
        self.tipas = tipas
        self.suma = suma

    def __str__(self):
        # Apibreziame kaip konvertuoti irasa i eilute/stringa, kuris bus nuadojams spausdinat irasa
        return f"{self.tipas}: {self.suma}"


# Sukursime klase Biudzetas kurioje ura daug pajamu ir islaidu irasu
class Biudzetas:
    def __init__(self):
        # Inicijuojame zurnala su tursciu irasu sarasu
        self.zurnalas = []

    def prideti_pajamu_irasa(self, suma):
        # Pridesime pajamu irasa i biudzeta, zurnalo sarasa
        self.zurnalas.append(Irasas("Pajamos", suma))

    def prideti_islaidu_irasa(self, suma):
        # Pridesime islaidu irasa i biudzeta, zurnalo sarasa
        self.zurnalas.append(Irasas("Islaidos", -suma))

    def gauti_balansa(self):
        # Apskaiciuosime ir grazinsime biudzeto balansa, kuris bus visu irasu sumu suma
        return sum(irasa.suma for irasa in self.zurnalas)

    def parodyti_ataskaita(self):
        # Spausdiname visus biudzeto irasus
        for irasas in self.zurnalas:
            print(irasas)

# Sukusrime biudzeta
biudzetas = Biudzetas()


# Pradesime cikla, kuris bus vykdomas, kol mes nusprendziame programa isjungti
while True:
    print("1. Ivesti pajamas")
    print("2. Ivest islaidas")
    print("3. Parodyti balansa")
    print("4. Parodyti ataskaita")
    print("5. Iseiti is programos")

    pasirinkimas = input("Pasirinkite veiksma: ")

    # Tikrinsime kuri pasirinkima vykdyti
    if pasirinkimas == "1":
        suma = float(input("Iveskite pajamu suma: "))
        biudzetas.prideti_pajamu_irasa(suma)

    elif pasirinkimas == "2":
        suma = float(input("Iveskite isladu suma: "))
        biudzetas.prideti_islaidu_irasa(suma)

    elif pasirinkimas == "3":
        print(f"Balansas: {biudzetas.gauti_balansa()}")

    elif pasirinkimas == "4":
        biudzetas.parodyti_ataskaita()

    elif pasirinkimas == "5":
        break

    else:
        print("Netinkamas pasirinkimas. Bandykite dar karta")
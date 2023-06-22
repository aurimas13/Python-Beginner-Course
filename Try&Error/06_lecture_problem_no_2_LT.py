from datetime import datetime, timedelta

class Darbuotojas:
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = dirba_nuo

    # Privatus metodas, kuris paskaičiuoja, kiek darbuotojas nudirbo dienų nuo įvestos dienos iki šiandien
    def __dirbo_dienos(self):
        return (datetime.now() - self.dirba_nuo).days

    # Metodas, kuris paskaičiuoja bendrą atlyginimą
    def paskaiciuoti_atlyginima(self):
        return self.__dirbo_dienos() * self.valandos_ikainis * 8

class NormalusDarbuotojas(Darbuotojas):
    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        super().__init__(vardas, valandos_ikainis, dirba_nuo)

    # Perrašomas privatus metodas, kuris paskaičiuoja, kiek darbuotojas nudirbo dienų nuo įvestos dienos iki šiandien
    def __dirbo_dienos(self):
        # Čia skaičiuojamos tik darbo dienos (5 dienos per savaitę)
        return (datetime.now() - self.dirba_nuo).days * 5 // 7

# Sukuriamas Darbuotojo objektas
darbuotojas = Darbuotojas("Jonas", 10, datetime.now() - timedelta(days=20))

# Sukuriamas NormalusDarbuotojas objektas
normalus_darbuotojas = NormalusDarbuotojas("Petras", 10, datetime.now() - timedelta(days=30))

# Paleidžiama funkcija paskaiciuoti_atlyginima su abiem objektais
print(darbuotojas.paskaiciuoti_atlyginima())
print(normalus_darbuotojas.paskaiciuoti_atlyginima())

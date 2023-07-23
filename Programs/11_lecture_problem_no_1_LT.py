class Namas:
    def __init__(self, plotas, verte):
        # Inicializuojame pradines savybes
        self._plotas = plotas
        self._verte = verte

    @property
    def plotas(self):
        # Grąžiname savybę "plotas"
        return self._plotas

    @property
    def verte(self):
        # Grąžiname savybę "vertė"
        return self._verte

    @verte.setter
    def verte(self, verte):
        # Tikriname, ar įvestas vertės tipas yra skaičius
        if isinstance(verte, (int, float)):
            # Jei taip, atnaujiname savybę "vertė"
            self._verte = verte
        else:
            # Jei ne, išmetame klaidą
            raise ValueError('Vertė turi būti skaičius!')

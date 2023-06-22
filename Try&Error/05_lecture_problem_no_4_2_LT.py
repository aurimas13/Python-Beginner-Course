import datetime
from datetime import datetime, timedelta

class Metines:
    def __init__(self, metai=1990, menesis=1, diena=1):  # Sukuriamas objektas su numatytąja data, jei data nėra pateikta
        self.data = datetime(metai, menesis, diena)

    def __str__(self):  # Metodas, kuris leidžia atspausdinti objektą kaip datą
        return self.data.strftime("%Y-%m-%d")  # Konvertuoja datą į eilutę formatu: metai-mėnuo-diena

    def time_since(self):  # Metodas, grąžinantis praėjusį laiką nuo nurodytų metinių
        dabar = datetime.now()
        skirtumas = dabar - self.data

        metai = skirtumas.days // 365
        savaites = skirtumas.days // 7
        dienos = skirtumas.days
        valandos = skirtumas.seconds // 3600
        minutes = skirtumas.seconds // 60
        sekundes = skirtumas.seconds

        return metai, savaites, dienos, valandos, minutes, sekundes

    def is_leap_year(self):  # Metodas, patikrinantis ar metinių metai buvo keliamieji
        metai = self.data.year
        return metai % 4 == 0 and (metai % 100 != 0 or metai % 400 == 0)

    def subtract_days(self, dienos):  # Metodas, atimantis nurodytą dienų skaičių nuo datos ir grąžinantis naują datą
        nauja_data = self.data - timedelta(days=dienos)
        return nauja_data

    def add_days(self, dienos):  # Metodas, pridedantis nurodytą dienų skaičių prie datos ir grąžinantis naują datą
        nauja_data = self.data + timedelta(days=dienos)
        return nauja_data

a = Metines(2000, 1, 1)
print(a)  # Tai atspausdins: 2000-01-01

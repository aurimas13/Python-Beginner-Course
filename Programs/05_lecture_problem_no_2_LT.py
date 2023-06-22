# Importuojame datetime ir timedelta funkcijas iš datetime modulio
from datetime import datetime, timedelta

# Sukuriam Anniversary klasę
class Anniversary:
    # Klasės konstruktorius, priimantis metus, mėnesį ir dieną
    def __init__(self, year, month, day):
        # Sukuriame datą ir priskiriame ją klasės atributui
        self.date = datetime(year, month, day)

    # Metodas, kuris grąžina praėjusį laiką nuo nurodytos datos
    def time_since(self):
        # Gauname dabartinę datą
        now = datetime.now()
        # Skaičiuojame skirtumą tarp dabartinės ir nurodytos datos
        difference = now - self.date

        # Skaičiuojame praėjusius metus, savaites, dienas, valandas, minutes ir sekundes
        years = difference.days // 365
        weeks = difference.days // 7
        days = difference.days
        hours = difference.seconds // 3600
        minutes = difference.seconds // 60
        seconds = difference.seconds

        # Grąžiname gautus rezultatus
        return years, weeks, days, hours, minutes, seconds

    # Metodas, kuris tikrina, ar metus, kuriems priklauso data, buvo keliamieji
    def is_leap_year(self):
        # Gauname metus iš datos
        year = self.date.year
        # Tikriname, ar metai yra keliamieji
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    # Metodas, kuris atima nurodytą dienų skaičių nuo datos ir grąžina naują datą
    def subtract_days(self, days):
        # Skaičiuojame naują datą
        new_date = self.date - timedelta(days=days)
        # Grąžiname naują datą
        return new_date

    # Metodas, kuris prideda nurodytą dienų skaičių prie datos ir grąžina naują datą
    def add_days(self, days):
        # Skaičiuojame naują datą
        new_date = self.date + timedelta(days=days)
        # Grąžiname naują datą
        return new_date


# Klasės testavimas
# Sukuriam naują Anniversary objektą su 2000 metų sausio 1 d. data
a = Anniversary(2000, 1, 1)
# Spausdiname praėjusį laiką nuo nurodytos datos
print(a.time_since())
# Tikriname, ar 2000 metai buvo keliamieji
print(a.is_leap_year())
# Atimame 365 dienas nuo nurodytos datos ir spausdiname gautą datą
print(a.subtract_days(365))
# Pridedame 365 dienas prie nurodytos datos ir spausdiname gautą datą
print(a.add_days(365))

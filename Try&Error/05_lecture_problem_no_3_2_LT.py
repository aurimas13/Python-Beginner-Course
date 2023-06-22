from datetime import datetime, timedelta


class Metines:
    # Konstruktorius, kuris priima metus, mėnesį ir dieną. Jei data nenurodoma, naudojamas numatytasis programuotojo gimtadienis
    def __init__(self, year=1990, month=1, day=1):  
        self.date = datetime(year, month, day)

    # Metodas, kuris grąžina praejusį laiką nuo nurodytų metinių
    def time_since(self):  
        now = datetime.now()
        difference = now - self.date

        years = difference.days // 365
        weeks = difference.days // 7
        days = difference.days
        hours = difference.seconds // 3600
        minutes = difference.seconds // 60
        seconds = difference.seconds

        return years, weeks, days, hours, minutes, seconds

    # Metodas, kuris tikrina, ar metinių metai buvo keliamieji
    def is_leap_year(self):  
        year = self.date.year
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    # Metodas, kuris atima nurodytą dienų skaičių nuo datos ir grąžina naują datą
    def subtract_days(self, days):  
        new_date = self.date - timedelta(days=days)
        return new_date

    # Metodas, kuris prideda nurodytą dienų skaičių prie datos ir grąžina naują datą
    def add_days(self, days):  
        new_date = self.date + timedelta(days=days)
        return new_date

# Sukuriamas ir testuojamas objektas su numatytąja data (programuotojo gimtadienis)
a = Metines()
print(a.time_since())
print(a.is_leap_year())
print(a.subtract_days(365))
print(a.add_days(365))

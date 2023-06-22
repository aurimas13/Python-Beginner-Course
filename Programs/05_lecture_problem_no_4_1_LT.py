import re

print("Hello, world!")

class Sakinys:
    def __init__(self, tekstas="numatytasis"):  # Sukuriamas objektas su numatytuoju tekstu, jei tekstas nėra pateiktas
        self.tekstas = tekstas

    def __str__(self):  # Metodas, kuris leidžia atspausdinti objektą kaip tekstą
        return self.tekstas
   
    def reverse_text(self):  # Metodas, grąžinantis tekstą atvirkščiai
        return self.tekstas[::-1]

    def to_lowercase(self):  # Metodas, grąžinantis tekstą mažosiomis raidėmis
        return self.tekstas.lower()

    def to_uppercase(self):  # Metodas, grąžinantis tekstą didžiosiomis raidėmis
        return self.tekstas.upper()

    def get_word_by_index(self, indeksas):  # Metodas, grąžinantis žodį pagal jo eilės numerį sakinyje
        zodziai = self.tekstas.split()  # Tekstas skaidomas į žodžius
        if indeksas < len(zodziai):  # Patikrinama, ar indeksas yra teksto ribose
            return zodziai[indeksas]  # Grąžinamas nurodyto indekso žodis
        return "Indeksas yra už ribų"  # Grąžinamas klaidos pranešimas, jei indeksas yra už ribų

    def count_occurrences(self, elementas):  # Metodas, grąžinantis nurodyto simbolio ar žodžio pasikartojimų skaičių tekste
        return self.tekstas.count(elementas)

    def replace_item(self, senas_elementas, naujas_elementas):  # Metodas, grąžinantis tekstą, kuriame nurodytas žodis ar simbolis pakeistas
        return self.tekstas.replace(senas_elementas, naujas_elementas)

    def print_info(self):  # Metodas, spausdinantis žodžių, skaičių, didžiųjų ir mažųjų raidžių skaičių sakinyje
        zodziai = len(re.findall(r'\b\w+\b', self.tekstas))  # Skaičiuojami žodžiai
        skaiciai = len(re.findall(r'\b\d+\b', self.tekstas))  # Skaičiuojami skaičiai
        didziosios = len(re.findall(r'[A-Z]', self.tekstas))  # Skaičiuojamos didžiosios raidės
        mazosios = len(re.findall(r'[a-z]', self.tekstas))  # Skaičiuojamos mažosios raidės

        print(f"Žodžiai: {zodziai}, Skaičiai: {skaiciai}, Didžiosios: {didziosios}, Mažosios: {mazosios}")  
        

if __name__ == '__main__':
    s = Sakinys("As esu Aurimas")
    s.print_info()

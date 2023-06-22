import re  # Importuojame reguliariųjų išraiškų (regex) modulį

class Sakinys:
    # Konstruktorius, kuris priima tekstą. Jei tekstas nenurodomas, naudojamas numatytasis tekstas "Pasaulis yra mano"
    def __init__(self, text="Pasaulis yra mano"):  
        self.text = text

    # Metodas, kuris grąžina tekstą atvirkštine tvarka
    def reverse_text(self):  
        return self.text[::-1]

    # Metodas, kuris grąžina tekstą mažosiomis raidėmis
    def to_lowercase(self):  
        return self.text.lower()

    # Metodas, kuris grąžina tekstą didžiosiomis raidėmis
    def to_uppercase(self):  
        return self.text.upper()

    # Metodas, kuris grąžina žodį pagal jo numerį sakinio žodžių sekoje, kur indeksas yra 1
    def get_word_by_index(self, index=1):  
        words = self.text.split()  # Skaidome tekstą į žodžius
        if index < len(words):  # Tikriname, ar indeksas yra reikšmių ribose
            return words[index]  # Grąžiname žodį pagal nurodytą indeksą
        return "Indeksas yra už ribų"  # Grąžiname klaidos pranešimą, jei indeksas yra už ribų

    # Metodas, kuris grąžina nurodyto simbolio ar žodžio pasikartojimų tekste skaičių
    def count_occurrences(self, item):  
        return self.text.count(item)

    # Metodas, kuris grąžina tekstą, kuriame nurodytas žodis ar simbolis pakeistas nauju, kur old_item yra "Jonas", o new_item yra "Simas"
    def replace_item(self, old_item="Jonas", new_item="Simas"):  
        return self.text.replace(old_item, new_item)

    # Metodas, kuris atspausdina žodžių, skaičių, didžiųjų ir mažųjų raidžių sakinio skaičių
    def print_info(self):  
        words = len(re.findall(r'\b\w+\b', self.text))  # Skaičiuojame žodžius
        numbers = len(re.findall(r'\b\d+\b', self.text))  # Skaičiuojame skaičius
        uppercase = len(re.findall(r'[A-Z]', self.text))  # Skaičiuojame didžiąsias raides
        lowercase = len(re.findall(r'[a-z]', self.text))  # Skaičiuojame mažąsias raides

        # Atspausdiname informaciją
        print(f"Žodžiai: {words}, Skaičiai: {numbers}, Didžiosios raidės: {uppercase}, Mažosios raidės: {lowercase}")


if __name__ == "__main__":
    s = Sakinys("As esu Aurimas")
    s.print_info()
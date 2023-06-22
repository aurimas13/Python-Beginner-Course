import re  # Importuojame reguliariųjų išraiškų (regex) modulį

# Aprašome Sakinio klasę
class Sentence:
    def __init__(self, text):  # Inicializuojame klasę su teksto atributu
        self.text = text

    # Metodas grąžinantis tekstą atbulai
    def reverse_text(self):
        return self.text[::-1]

    # Metodas grąžinantis tekstą mažosiomis raidėmis
    def to_lowercase(self):
        return self.text.lower()

    # Metodas grąžinantis tekstą didžiosiomis raidėmis
    def to_uppercase(self):
        return self.text.upper()

    # Metodas grąžinantis žodį pagal jo eiliškumo numerį sakinyje
    def get_word_by_index(self, index):
        words = self.text.split()  # Skaidome tekstą į žodžius
        if index < len(words):  # Tikriname, ar indeksas yra diapazone
            return words[index]  # Grąžiname žodį pagal nurodytą indeksą
        return "Indeksas už ribų"  # Grąžiname klaidos pranešimą, jei indeksas yra už ribų

    # Metodas grąžinantis nurodyto simbolio ar žodžio kiekį tekste
    def count_occurrences(self, item):
        return self.text.count(item)

    # Metodas grąžinantis tekstą su pakeistu nurodytu žodžiu ar simboliu
    def replace_item(self, old_item, new_item):
        return self.text.replace(old_item, new_item)

    # Metodas spausdinantis informaciją apie žodžių, skaičių, didžiųjų ir mažųjų raidžių kiekį sakinyje
    def print_info(self):
        words = len(re.findall(r'\b\w+\b', self.text))  # Skaičiuojame žodžius
        numbers = len(re.findall(r'\b\d+\b', self.text))  # Skaičiuojame skaičius
        uppercase = len(re.findall(r'[A-Z]', self.text))  # Skaičiuojame didžiąsias raides
        lowercase = len(re.findall(r'[a-z]', self.text))  # Skaičiuojame mažąsias raides

        # Spausdiname informaciją
        print(f"Žodžiai: {words}, Skaičiai: {numbers}, Didžiosios raidės: {uppercase}, Mažosios raidės: {lowercase}")


# Kuriamas ir testuojamas klasės objektas
s = Sentence("Sveiki, pasauli! 123")  # Sukuriamas klasės objektas
print(s.reverse_text())  # Testuojamas reverse_text
print(s.to_lowercase())  # Testuojamas to_lowercase metodas
print(s.to_uppercase())  # Testuojamas to_uppercase metodas
print(s.get_word_by_index(1))  # Testuojamas get_word_by_index metodas
print(s.count_occurrences('i'))  # Testuojamas count_occurrences metodas
print(s.replace_item('i', 'o'))  # Testuojamas replace_item metodas
s.print_info()  # Testuojamas print_info metodas

import logging
import math

# Sukuriame savo logger klasę, kuri fiksuos pranešimus tiek faile, tiek konsolėje
class CustomLogger:
    def __init__(self, log_file):
        self.log_file = log_file
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter("%(asctime)s, %(levelname)s, %(message)s")

        # Sukuriame fileHandler objektą, kuris įrašys pranešimus į failą
        fileHandler = logging.FileHandler(log_file)
        fileHandler.setFormatter(formatter)
        self.logger.addHandler(fileHandler)

        # Sukuriame streamHandler objektą, kuris išspausdins pranešimus į konsolę
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        self.logger.addHandler(streamHandler)

    def log(self, level, message):
        self.logger.log(level, message)

# Sukuriame savo logerį, nurodant norimą log failo pavadinimą
custom_logger = CustomLogger("log_file.log")

# Funkcija, kuri grąžina visų paduotų skaičių sumą
def sum_all(*args):
    try:
        result = sum(args)
        custom_logger.log(logging.INFO, f"Skaiciu {args} suma lygi: {result}")
        return result
    except Exception as e:
        custom_logger.log(logging.ERROR, f"Išimtis {type(e).__name__} kilo bandant suskaičiuoti sumą: {e}")
        return None  # Grąžiname "None", jei įvyko išimtis

# Funkcija, kuri grąžina paduoto skaičiaus šaknį
def square_root(number):
    try:
        result = math.sqrt(float(number))
        custom_logger.log(logging.INFO, f"Skaičiaus {number} šaknis yra: {result}")
        return result
    except ValueError as e:
        custom_logger.log(logging.ERROR, f"Išimtis {type(e).__name__} kilo bandant išskaičiuoti šaknį: {e}")
        return None  # Grąžiname "None", jei įvyko išimtis
    except Exception as e:
        custom_logger.log(logging.ERROR, f"Nežinoma išimtis: {e}")
        return None  # Grąžiname "None", jei įvyko išimtis

# Funkcija, kuri grąžina paduoto sakinio simbolių kiekį
def sentence_length(sentence):
    length = len(sentence)
    custom_logger.log(logging.INFO, f"Sakinio '{sentence}' simbolių kiekis yra: {length}")
    return length

# Funkcija, kuri grąžina rezultatą, skaičių x padalinus iš y
def divide(x, y):
    try:
        if y == 0:
            raise ZeroDivisionError("Dalyba iš nulio negalima.")
        result = x / y
        custom_logger.log(logging.INFO, f"Rezultatas, kai {x} padaliname iš {y}, yra: {result}")
        return result
    except ZeroDivisionError as e:
        custom_logger.log(logging.ERROR, f"Išimtis {type(e).__name__} kilo dalybos metu: {e}")
        return None  # Grąžiname "None", jei įvyko išimtis
    except Exception as e:
        custom_logger.log(logging.ERROR, f"Nežinoma išimtis: {e}")
        return None  # Grąžiname "None", jei įvyko išimtis

# Testuojame funkcijas
print(sum_all(1, 2, 3, 4, 5))                  # Rezultatas: 15
print(sum_all("1", "2", 3, 4, 5))              # Išimtis bus įrašyta į log failą ir išspausdinta konsolėje
print(square_root(16))                         # Rezultatas: 4.0
print(square_root("16"))                       # Išimtis bus įrašyta į log failą ir išspausdinta konsolėje
print(sentence_length("Labas, pasauli!"))      # Rezultatas: 15
print(divide(10, 2))                           # Rezultatas: 5.0
print(divide(10, 0))                           # Išimtis bus įrašyta į log failą ir išspausdinta konsolėje, bet programa tęs veikimą

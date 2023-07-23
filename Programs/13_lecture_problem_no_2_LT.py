import logging
import math

# Nustatome log failo pavadinimą
log_file = "log_file.log"

# Sukuriame logger
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s, %(levelname)s, %(message)s")

# Funkcija, kuri grąžina visų paduotų skaičių sumą
def sum_all(*args):
    logging.info(f"Skaiciu {args} suma lygi: {sum(args)}")
    return sum(args)

# Funkcija, kuri grąžina paduoto skaičiaus šaknį
def custom_square_root(number):
    try:
        result = math.sqrt(float(number))
        logging.info(f"Skaičiaus {number} šaknis yra: {result}")
        return result
    except ValueError as e:
        logging.exception(f"Išimtis kilo bandant išskaičiuoti šaknį: {e}")
        return None  # Grąžiname "None", jei įvyko išimtis
    except Exception as e:
        logging.exception(f"Nežinoma išimtis: {e}")
        return None  # Grąžiname "None", jei įvyko išimtis

# Funkcija, kuri grąžina paduoto sakinio simbolių kiekį
def sentence_length(sentence):
    length = len(sentence)
    logging.info(f"Sakinio '{sentence}' simbolių kiekis yra: {length}")
    return length

# Funkcija, kuri grąžina rezultatą, skaičių x padalinus iš y
def divide(x, y):
    try:
        result = x / y
        logging.info(f"Rezultatas, kai {x} padaliname iš {y}, yra: {result}")
        return result
    except ZeroDivisionError as e:
        logging.exception(f"Išimtis kilo dalybos metu: {e}")
        return None  # Grąžiname "None", jei įvyko išimtis
    except Exception as e:
        logging.exception(f"Nežinoma išimtis: {e}")
        return None  # Grąžiname "None", jei įvyko išimtis

# Testuojame funkcijas
print(sum_all(1, 2, 3, 4, 5))                  # Rezultatas: 15
print(custom_square_root(16))                  # Rezultatas: 4.0
print(custom_square_root("16"))                # Išimtis bus įrašyta į log failą
print(sentence_length("Labas, pasauli!"))      # Rezultatas: 15
print(divide(10, 2))                           # Rezultatas: 5.0
print(divide(10, 0))                           # Išimtis bus įrašyta į log failą

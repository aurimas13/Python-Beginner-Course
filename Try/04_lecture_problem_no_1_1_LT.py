# Gražinti trijų paduotų skaičių sumą
def sum_three_numbers(a, b, c):
    return a + b + c

# Gražinti paduoto sąrašo iš skaičių sumą
def sum_list_numbers(numbers):
    return sum(numbers)

# Atspausdinti didžiausią iš kelių paduotų skaičių (panaudojant *args)
def print_max_number(*args):
    max_number = max(args)
    print(max_number)

# Gražinti paduotą stringą atbulai
def reverse_string(string):
    return string[::-1]

# Atspausdinti, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių
def count_characters(string):
    words = string.split()
    num_words = len(words)
    num_uppercase = sum(1 for char in string if char.isupper())
    num_lowercase = sum(1 for char in string if char.islower())
    num_digits = sum(1 for char in string if char.isdigit())

    print("Žodžių skaičius:", num_words)
    print("Didžiųjų raidžių skaičius:", num_uppercase)
    print("Mažųjų raidžių skaičius:", num_lowercase)
    print("Skaičių skaičius:", num_digits)

# Gražinti sąrašą tik su unikaliais paduoto sąrašo elementais
def unique_elements(lst):
    return list(set(lst))

# Gražinti, ar paduotas skaičius yra pirminis
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Išrikiuoti paduoto stringo žodžius nuo paskutinio iki pirmojo
def reverse_words(string):
    words = string.split()
    reversed_words = " ".join(reversed(words))
    return reversed_words

# Gražinti, ar paduoti metai yra keliamieji, ar ne
def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

# Atspausdinti, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių
def print_time_elapsed(years, months, days, hours, minutes, seconds):
    print("Metai:", years)
    print("Mėnesiai:", months)
    print("Dienos:", days)
    print("Valandos:", hours)
    print("Minutės:", minutes)
    print("Sekundės:", seconds)

# Pavyzdžiai

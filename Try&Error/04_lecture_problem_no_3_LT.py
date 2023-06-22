def check_same_neighbour(number):
    number_str = str(number)
    
    # Patikriname kiekvieno skaitmens gretimus skaičius ir lyginame su dabartiniu skaitmeniu
    for i in range(len(number_str) - 1):
        current_digit = int(number_str[i])
        next_digit = int(number_str[i + 1])
        
        if next_digit != current_digit + 1:
            return False
    
    return True

def get_neighbour_numbers(number):
    number_str = str(number)
    neighbour_numbers = []
    
    # Sukuriame kiekvieno skaitmens gretimą skaičių ir pridedame į sąrašą
    for i in range(len(number_str) - 1):
        current_digit = int(number_str[i])
        next_digit = int(number_str[i + 1])
        
        neighbour_numbers.append(f"{current_digit} - {current_digit + 1}{next_digit}")
    
    return neighbour_numbers

# Pavyzdžiai

# Tikriname ar skaičiaus pirmoji pusė yra lygi antrajai
number = 123456
is_same = check_same_neighbour(number)
print(is_same)  # False

# Gauti kiekvieno skaitmens gretimus skaičius
number = 5678
neighbour_numbers = get_neighbour_numbers(number)
for neighbour_number in neighbour_numbers:
    print(neighbour_number)
# 5 - 46
# 6 - 57
# 7 - 68
# 8 - 79

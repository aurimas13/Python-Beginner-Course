s = "Labas, pasauli!"

# Funkcija upper() pavers visus raides didžiosiomis raidėmis
s_upper = s.upper()
print(s_upper)  # Rezultatas: LABAS, PASAULI!

# Funkcija casefold() pakeis tekstą į mažąsias raides ir pašalins specifinius ženklus
s_casefolded = s.casefold()
print(s_casefolded)  # Rezultatas: labas, pasauli!

# Funkcija capitalize() pavers pirmą raidę didžiąja, o kitas raides - mažosiomis
s_capitalized = s.capitalize()
print(s_capitalized)  # Rezultatas: Labas, pasauli!

# Funkcija count() grąžina simbolių pasikartojimų skaičių tekste
count_a = s.count('a')
print(count_a)  # Rezultatas: 3

# Funkcija find() gražina pirmos pasitaikančios simbolio vietą tekste, jei neranda -1
position_s = s.find('s')
print(position_s)  # Rezultatas: 3


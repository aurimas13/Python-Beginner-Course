import requests
from bs4 import BeautifulSoup
import re

url = 'https://www.telia.lt/prekes/mobilieji-telefonai/samsung'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Raskime visus elementus su klase "mobiles-product-card__price-marker"
price_elements = soup.find_all('div', class_='mobiles-product-card__price-marker')

# Funkcija, kuri išgrynina kainą kaip sveikąjį skaičių
def extract_price(price_text):
    # Pašaliname visus ne skaitinius simbolius iš kainos teksto, išskyrus taškus (dešimtainių skyrių ženklus)
    price_text = re.sub(r'[^\d.]', '', price_text)
    # Konvertuojame tekstą į skaičių su kableliu (floating point) ir po to į sveikąjį skaičių (suapvalinant iki artimiausio sveikojo skaičiaus)
    return int(float(price_text))

# Išgryniname ir saugome visas kainas kaip sveikuosius skaičius
prices = [extract_price(price_element.text) for price_element in price_elements]

# Randame mažiausią ir didžiausią kainą
min_price = min(prices)
max_price = max(prices)

print("Mažiausia kaina yra:", min_price, "€")
print("Didžiausia kaina yra:", max_price, "€")

# from bs4 import BeautifulSoup
# import requests
# import csv

# source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung').text
# soup = BeautifulSoup(source, 'html.parser')

# blokai = soup.find_all('div', class_='mobiles-product-card__price-block')

# with open('Telia_Samsung_telefonai.csv', "w", encoding="UTF-8", newline='') as failas:

#     csv_writer = csv.writer(failas)
#     csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])
#     for blokas in blokai:
#         try:
#             pavadinimas = blokas.find('a', class_='mobiles-product-card__title').text.strip()
#             men_kaina = blokas.find('div', class_='mobiles-product-card__price-marker').text.strip()
#             kaina = blokas.find('div', class_='mobiles-product-card__full-price price').next_element.text.strip()
#             csv_writer.writerow([pavadinimas, men_kaina, kaina])
#         except:
#             pass

from bs4 import BeautifulSoup
import requests
import csv
import json
import re

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung').text
soup = BeautifulSoup(source, 'html.parser')

# Find the script tag containing the data
script_tag = soup.find('script', string=re.compile('var categoryProducts = \['))

# Extract the JSON data from the script tag
json_text = re.search('var categoryProducts = (\[.*?\]);', script_tag.string, flags=re.S).group(1)

# Parse the JSON data
products = json.loads(json_text)

with open('Telia_Samsung_telefonai.csv', "w", encoding="UTF-8", newline='') as failas:
    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Modelis', 'Kaina', 'ID', 'Pozicija'])

    for product in products:
        modelis = product['name']
        kaina = product['price']
        id = product['id']
        pozicija = product['position']

        csv_writer.writerow([modelis, kaina, id, pozicija])

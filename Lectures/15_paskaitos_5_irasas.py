from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.telia.lt/prekes/mobilieji-telefonai/samsung').text
soup = BeautifulSoup(source, 'html.parser')

blokai = soup.find_all('div', class_='mobiles-product-card__price-block')

with open('Telia_Samsung_telefonai.csv', "w", encoding="UTF-8", newline='') as failas:

    csv_writer = csv.writer(failas)
    csv_writer.writerow(['Modelis', 'Mėnesio kaina', 'Kaina'])
    for blokas in blokai:
        try:
            pavadinimas = blokas.find('a', class_='mobiles-product-card__title').text.strip()
            men_kaina = blokas.find('div', class_='mobiles-product-card__price-marker').text.strip()
            kaina = blokas.find('div', class_='mobiles-product-card__full-price price').next_element.text.strip()
            csv_writer.writerow([pavadinimas, men_kaina, kaina])
        except:
            pass

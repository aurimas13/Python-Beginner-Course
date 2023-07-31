from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
blokai = soup.find_all('div', class_='headline')

for blokas in blokai:
    try:
        kategorija = blokas.find('div', class_='headline-category').text.strip()
        tekstas = blokas.find('a', class_='CBarticleTitle').text.strip()
        print(kategorija)
        print(tekstas)
    except:
        pass

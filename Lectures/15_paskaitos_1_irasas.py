from bs4 import BeautifulSoup
import requests

source = requests.get('https://www.delfi.lt/').text
soup = BeautifulSoup(source, 'html.parser')
blokas = soup.find('div', class_='headline')
print(blokas.prettify())
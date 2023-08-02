from bs4 import BeautifulSoup
import requests

url = 'https://www.delfi.lt'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

antrastes = soup.find_all('h1')
print(f"Šiandienos antraštinių straipsnių skaičius: {len(antrastes)}")

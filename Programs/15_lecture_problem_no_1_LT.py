import requests
from bs4 import BeautifulSoup

# Nurodykime URL, iš kurio norime parsisiųsti informaciją
url = 'https://www.15min.lt'

# Atlikime užklausą į nurodytą URL ir gaukime atsakymą
response = requests.get(url)

# Naudodami BeautifulSoup, analizuokime gautą HTML dokumentą
soup = BeautifulSoup(response.text, 'html.parser')

# Suraskime visus <a> žymės elementus, turinčius atributą "data-ga-track" su reikšme "w_Redakcija_rekomenduoja"
rekomenduojami_straipsniai = soup.find_all('a', {'data-ga-track': 'w_Redakcija_rekomenduoja'})

# Išgryninkime ir spausdiname "img alt" tekstą ir teksto, esančio po <span> žymės su klase 'title', turinį <a> žymėse
for straipsnis in rekomenduojami_straipsniai:
    img_zyme = straipsnis.find('img')
    span_zyme = straipsnis.find('span', class_='title')
    
    # Jei yra <img> žymė, išgryninkime ir spausdiname "img alt" tekstą
    if img_zyme:
        img_alt = img_zyme.get('alt')
        print(img_alt)
    # Jei yra <span> žymė su klase 'title', išgryninkime ir spausdiname jos turinį
    elif span_zyme:
        span_tekstas = span_zyme.text.strip()
        print(span_tekstas)
    else:
        continue
    print()

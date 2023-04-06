import requests
from bs4 import BeautifulSoup as bs


URL = 'https://www.ss.com/ru/transport/cars/bmw/'
r = requests.get(URL)
soup = bs(r.text, 'html.parser')
cars = soup.find_all("td", {"class": "msga2-o pp6"})
for i in range(0, len(cars), 4):
    if i:
        model = cars[i].text.strip()
        year = cars[i+1].text.strip()
        engine = cars[i+2].text.strip()
        price = cars[i+3].text.strip()
        print(f"Модель: {model}\nГод: {year}\nДвигатель: {engine}\nЦена: {price}")



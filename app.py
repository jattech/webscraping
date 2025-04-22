from bs4 import BeautifulSoup
import os

with open(f"{os.getcwd()}/index.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')

lista_items = soup.find_all('li')

for item in lista_items:
    print(item)

#for item in lista_items:
#    print(item.text)



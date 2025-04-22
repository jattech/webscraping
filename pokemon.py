import requests
from bs4 import BeautifulSoup

url = "https://www.wikidex.net/wiki/Lista_de_Pok%C3%A9mon"
response = requests.get(url)
response.encoding = 'utf-8'  
soup = BeautifulSoup(response.text, "html.parser")

table = soup.find_all('table', {'class': 'tabpokemon'})[0]

if table:
    for row in table.find_all("tr"):
        cells = row.find_all("td")
        if len(cells) > 3:  # Asegúrate de que haya suficientes celdas
            numero = cells[0].text.strip()
            if numero == '0001':
                print(row)
            pokemon_name_element = cells[1].find("a")
            pokemon_name = pokemon_name_element.text.strip() if pokemon_name_element else "N/A"

            tipos = []
            tipo_elements = cells[2].find_all("a")
            for tipo_element in tipo_elements:
                tipos.append(tipo_element.get("title", "N/A").replace("Tipo ", ""))

            print(f"Id: {numero}, Nombre: {pokemon_name}, Tipo: {', '.join(tipos)}")
else:
    print("No se encontró la tabla en la página.")
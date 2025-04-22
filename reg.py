import re
import requests

def scrape_titles(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lanza una excepción para códigos de estado HTTP malos (4xx o 5xx)
        html = response.text
        title_pattern = r"<title>(.*?)</title>"
        titles = re.findall(title_pattern, html, re.IGNORECASE)
        return titles
    except requests.exceptions.RequestException as e:
        print(f"Error al acceder a la URL: {e}")
        return []
    except re.error as e:
        print(f"Error en la expresión regular: {e}")
        return []

if __name__ == "__main__":
    target_url = "https://nuclio.school"
    found_titles = scrape_titles(target_url)

    if found_titles:
        print("Títulos encontrados:")
        for title in found_titles:
            print(f"- {title.strip()}")
    else:
        print("No se encontraron títulos en la página.")
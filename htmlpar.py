from html.parser import HTMLParser
import os

class MiHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.enlace_actual = None
        self.titulos = []
        self.enlaces = []
        self.dentro_titulo = False

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.dentro_titulo = True
        elif tag == 'a':
            self.enlace_actual = dict(attrs).get('href')

    def handle_endtag(self, tag):
        if tag == 'title':
            self.dentro_titulo = False
        elif tag == 'a':
            if self.enlace_actual:
                self.enlaces.append(self.enlace_actual)
                self.enlace_actual = None

    def handle_data(self, data):
        if self.dentro_titulo:
            self.titulos.append(data.strip())

# Crear una instancia de nuestro parser personalizado
parser = MiHTMLParser()

# Alimentar el HTML al parser
# Ruta del archivo index.html
file_path = f"{os.getcwd()}/index.html"

# Leer el contenido del archivo
with open(file_path, 'r') as file:
    
    content = file.read()
    parser.feed(content)

    # Acceder a la información extraída
    if parser.titulos:
        print("Título de la página:", parser.titulos[0])

    if parser.enlaces:
        print("\nEnlaces encontrados:")
        for enlace in parser.enlaces:
            print(f"- {enlace}")

    # Cerrar el parser
    parser.close()
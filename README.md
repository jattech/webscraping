# Proyecto de Web Scraping

Este proyecto contiene varios scripts en Python diseñados para realizar tareas de web scraping y análisis de contenido HTML. A continuación, se describe la funcionalidad de cada archivo en el proyecto.

## Estructura del Proyecto
├── app.py ├── htmlpar.py ├── index.html ├── pokemon.py ├── reg.py


### Archivos y Descripción

#### `app.py`
Este script utiliza la biblioteca `BeautifulSoup` para analizar el archivo HTML local `index.html`. Extrae y muestra todos los elementos `<li>` de la lista no ordenada presente en el archivo.

#### `htmlpar.py`
Este archivo implementa un parser HTML personalizado utilizando la clase `HTMLParser` de la biblioteca estándar de Python. Su funcionalidad incluye:
- Extraer el título de la página HTML.
- Extraer todos los enlaces (`<a href="...">`) del archivo `index.html`.

#### `index.html`
Un archivo HTML de ejemplo que sirve como fuente de datos para los scripts `app.py` y `htmlpar.py`. Contiene:
- Un título (`<title>`).
- Una lista no ordenada con elementos `<li>`.
- Un enlace (`<a>`).

#### `pokemon.py`
Este script realiza scraping de la página de Wikidex para obtener información sobre Pokémon. Extrae:
- El número de identificación del Pokémon.
- El nombre del Pokémon.
- Los tipos asociados al Pokémon.

#### `reg.py`
Este archivo utiliza expresiones regulares para extraer el título de una página web dada una URL. Hace uso de la biblioteca `requests` para realizar solicitudes HTTP.

### Requisitos

Para ejecutar los scripts, asegúrate de tener instaladas las siguientes bibliotecas:

- `requests`
- `beautifulsoup4`

Puedes instalarlas ejecutando:

```bash
pip install requests beautifulsoup4

Uso
app.py: Ejecuta el script para analizar el archivo index.html y mostrar los elementos <li>:

htmlpar.py: Ejecuta el script para extraer el título y los enlaces del archivo index.html:

pokemon.py: Ejecuta el script para obtener información sobre Pokémon desde Wikidex:

reg.py: Ejecuta el script para extraer el título de una página web dada una URL:

Notas
Asegúrate de tener conexión a Internet para los scripts que realizan solicitudes HTTP (pokemon.py y reg.py).
El archivo index.html debe estar en el mismo directorio que los scripts para que app.py y htmlpar.py funcionen correctamente.
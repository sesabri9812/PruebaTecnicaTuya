README.md
HTML Processor – Codificación de Imágenes a Base64
Descripción del proyecto

Este proyecto tiene como objetivo procesar archivos HTML, identificar las imágenes locales referenciadas en ellos, convertir estas imágenes a formato Base64 y generar nuevas versiones de los archivos HTML con las imágenes embebidas. Además, se genera un reporte indicando qué imágenes fueron procesadas exitosamente y cuáles fallaron.

La solución está diseñada siguiendo buenas prácticas de programación, utilizando programación orientada a objetos (OOP) y únicamente librerías de la Python Standard Library, cumpliendo los requerimientos de la prueba técnica.

Estructura del proyecto
html-processor/
│
├── src/
│   ├── encoder/
│   │   └── image_encoder.py        # Clase para codificar imágenes a Base64
│   │
│   ├── finder/
│   │   └── html_finder.py          # Clase para descubrir archivos HTML en rutas y subdirectorios
│   │
│   ├── parser/
│   │   └── html_parser.py          # Clase para parsear HTML, identificar y reemplazar imágenes
│   │
│   ├── processor/
│   │   └── html_processor.py       # Orquestador principal que coordina la ejecución completa
│
├── data/
│   ├── input/                      # Archivos HTML originales
│   └── output/                     # Archivos HTML procesados
│
├── main.py                         # Entry point del proyecto
├── requirements.txt                # No requiere librerías externas
└── README.md
Arquitectura y diseño

El proyecto está estructurado siguiendo principios de SOLID y Clean Code:

Single Responsibility (SRP): Cada clase tiene una responsabilidad única:
HTMLFileFinder: localizar archivos HTML.
ImageEncoder: convertir imágenes a Base64.
HTMLImageParser: parsear HTML y reemplazar imágenes.
HTMLProcessor: orquestar el flujo completo de procesamiento.
Open/Closed (OCP): Las clases pueden extenderse sin modificar su implementación base, permitiendo agregar nuevos tipos de procesadores o formatos de archivo.
Encapsulamiento y Abstracción: Cada componente oculta su complejidad interna. Por ejemplo, el parser no necesita saber cómo se codifica la imagen, solo utiliza el ImageEncoder.
Desacoplamiento: El flujo de ejecución está separado en módulos, lo que permite probar y mantener cada componente de manera independiente.
Flujo de ejecución
Entrada: Se proporcionan rutas a archivos HTML individuales o directorios completos (con soporte para subdirectorios).
Descubrimiento de archivos: HTMLFileFinder recorre cada ruta y detecta todos los archivos con extensión .html.
Parsing y reemplazo de imágenes:
HTMLImageParser analiza cada archivo HTML utilizando HTMLParser de la biblioteca estándar.
Se identifican todas las etiquetas <img> y se obtiene el atributo src.
Cada imagen se codifica a Base64 usando ImageEncoder.
Se reemplaza el src original por la versión embebida data:image;base64,....
Generación de archivos nuevos:
Los archivos originales no se modifican.
Se crea un nuevo archivo con el sufijo _processed.html en el mismo directorio.
Reporte de procesamiento:
Se construye un objeto JSON con las imágenes procesadas exitosamente y las que fallaron, por archivo.
{
  "success": {
    "file1.html": ["img1.png", "img2.jpg"]
  },
  "fail": {
    "file1.html": ["img3.png"]
  }
}
Tecnologías utilizadas
Python 3.x
Standard Library:
html.parser → análisis de HTML.
pathlib → manejo de rutas de archivos y directorios.
base64 → codificación de imágenes.
typing → anotaciones de tipo.
os (opcional) → soporte de sistema de archivos.

No se utilizan librerías externas, cumpliendo el requerimiento del ejercicio.

Buenas prácticas implementadas
Código modular y organizado por responsabilidades.
Uso de OOP para escalabilidad y mantenibilidad.
Separación de código fuente (src) y datos (data).
Posibilidad de procesar múltiples archivos y directorios recursivamente.
Manejo de errores al codificar imágenes y registro de fallos.
Entry point main.py limpio, sin lógica compleja, solo orquestación.
Cómo ejecutar
Colocar los archivos HTML originales en data/input/ o especificar rutas/directorios al ejecutar.
Ejecutar el proyecto:
python main.py
Los archivos procesados se generarán con el sufijo _processed.html.
Se imprimirá en consola un objeto JSON indicando imágenes procesadas con éxito y fallidas.
Decisiones técnicas clave
Uso de HTMLParser: Evita dependencias externas y permite cumplir con el requisito de usar solo la Standard Library.
OOP y separación de responsabilidades: Facilita mantenimiento, extensión y pruebas unitarias.
Reemplazo de imágenes sin alterar archivos originales: Previene pérdida de datos y permite comparación.
Reporte de éxito/fallo por archivo: Permite control y auditoría de procesamiento.
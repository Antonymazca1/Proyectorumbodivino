#Rumbo Divino – Aplicación Web de Inspiración Cristiana

**Rumbo Divino** es una aplicación web personal de inspiración y motivación cristiana.  
Su propósito es compartir mensajes de fe, versículos bíblicos y permitir que las personas envíen peticiones de oración, integrando **frontend**, **backend en Python puro** y **almacenamiento de datos sin frameworks**.

---

## Tecnologías utilizadas

- **HTML5** – estructura del sitio  
- **CSS3** – diseño visual y estilos personalizados  
- **JavaScript** – interactividad y validaciones  
- **Python 3** – servidor backend (`http.server`)  
- **JSON** – almacenamiento de peticiones  
- **YouTube Embed** – reproducción de video inspiracional  

---

## Estructura del proyecto

```text
AplicacionWebPersonal/
│
├── server.py
├── README.md
│
├── templates/
│   ├── index.html
│   ├── about.html
│   ├── messages.html
│   ├── resources.html
│   ├── contact.html
│   ├── login.html
│   └── admin.html
│
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── main.js
│   └── img/
│       ├── banner.jpg
│       ├── logo.png
│       └── about.jpg
│
└── data/
    └── messages.json


## PASO 1: Instalar Python
Asegúrese de tener Python 3 instalado.

Verificar instalación:
```bash
python --version

Ejecutar el servidor
_______________________________
Abrir la terminal en Visual Studio Code.

Ejecutar:

python server.py
Si todo está correcto, se mostrará:

Servidor activo en http://localhost:8000
_________________________________________
Visualizar la aplicación

Abrir el navegador web.

Ingresar:

http://localhost:8000

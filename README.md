# Proyecto Urban Grocers - API Testing

## Descripción
Este proyecto contiene pruebas automatizadas para la API de Urban Grocers, enfocándose en la validación de la creación de kits de usuario. Las pruebas verifican diferentes escenarios de validación del campo "name" en los kits, incluyendo casos positivos y negativos.

## Requisitos Previos
- Python 3.14+ instalado
- Biblioteca `requests` para llamadas HTTP
- Biblioteca `pytest` para ejecución de pruebas
- Conexión a internet
- Servidor de Urban Grocers activo

## Instalación y Configuración (Git Bash)
### Paso 1: Clonar el repositorio
git clone [URL_del_repositorio]
cd qa-project-Urban-Grocers-app-es
### Paso 2: Instalar dependencias
pip install requests pytest
### Paso 3: Configurar URL del servidor
1. Abre el archivo configuration.py
2. Actualiza la variable URL_SERVICE con la URL actual del servidor
3. Importante: Los servidores son temporales, verifica que la URL esté activa
### Paso 4: Ejecutar las pruebas
#### Ejecutar todas las pruebas
pytest test.py -v
#### Ejecutar una prueba específica
pytest test.py::test_create_kit_1_letter_in_name_get_success_response -v

## Tecnologías Utilizadas
- Python: 3.14+
- Requests: Biblioteca para llamadas HTTP
- Pytest: Framework de testing
- API REST: Comunicación con servicios backend
- Git: Control de versiones

## Estructura del Proyecto
qa-project-Urban-Grocers-app-es/
├── test.py           # Casos de prueba principales
├── utilities.py      # Funciones auxiliares para llamadas HTTP
├── data.py           # Datos de prueba y headers
├── configuration.py  # Configuración de URLs y endpoints
├── README.md         # Documentación del proyecto
└── .gitignore        # Archivos ignorados por Git

### Modularidad Implementada
- test.py: Contiene los casos de prueba y funciones de validación
- utilities.py: Maneja las llamadas HTTP (GET/POST)
- data.py: Almacena datos de

## Funcionalidades Probadas
- ✅ Creación de kits con nombres válidos (1-511 caracteres)
- ✅ Validación de caracteres especiales y espacios
- ✅ Manejo de números como strings
- ❌ Validación de errores con nombres inválidos (vacío, muy largo, tipos incorrectos)

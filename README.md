# Proyecto ETL con Docker Compose

## Descripción
Este proyecto carga datos desde un archivo CSV a una base de datos PostgreSQL usando un contenedor de Docker. El sistema está orquestado con Docker Compose para incluir tanto la base de datos como la aplicación ETL.

## Requisitos
- Docker
- Docker Compose
- Tener un entorno donde se peuda ejecutar python y descargar sus librerías

## Estructura de Archivos
- `docker-compose.yml`: Configuració de los servicios de la base de datos y la aplicación Python.
- `Dockerfile`: Construye el contenedor de la aplicación ETL.
- `script.py`: Script Python que realiza la carga de datos.
- `requirements.txt`: Lista de dependencias para el script Python.
- `facts_table.csv`: Archivo de muestra con los datos a cargar.

## Instrucciones

1. Clona el repositorio o descarga el proyecto en tu máquina.
2. Asegúrate de que el archivo `facts_table.csv` esté en la raíz del proyecto.
3. Construye y ejecuta los contenedores con Docker Compose:
   ```bash
   docker compose up

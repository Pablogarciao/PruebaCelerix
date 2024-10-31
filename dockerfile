# FROM python:3.9-slim

# WORKDIR /app

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# COPY . .

# CMD ["python", "script.py"]

# Usa una imagen base de Python (ajusta la versión si es necesario)
FROM python:3.10

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia el archivo requirements.txt al contenedor
COPY requirements.txt .

# Instala dependencias del sistema necesarias para compilar psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Actualiza pip e instala los paquetes de Python listados en requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copia el resto de la aplicación al contenedor
COPY . .

# Comando de ejecución por defecto (ajusta según lo que necesites)
CMD ["python", "script.py"]

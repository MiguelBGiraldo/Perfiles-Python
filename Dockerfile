# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de tu proyecto al contenedor
COPY . /app/

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto en el que la app se ejecutará (por ejemplo, 8000)
EXPOSE 8000

# Comando para ejecutar la aplicación usando Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

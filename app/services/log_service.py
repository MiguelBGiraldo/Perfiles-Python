
import os
import requests
from pydantic import BaseModel

# Modelo para los logs
class LogRequest(BaseModel):
    application: str
    level: str  
    className: str  
    summary: str
    description: str  

# Función para enviar el log a la API
def send_log_to_api(log: LogRequest):
    try:
        # Convertir el objeto LogRequest a un diccionario para enviarlo como JSON

        api_url = os.getenv("API_LOGS_URL")

        log_data = log.model_dump()

        # Realizar la solicitud POST a la API de logs
        response = requests.post(api_url, json=log_data)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            print(f"Log enviado exitosamente: {log.message}")
        else:
            print(f"Error al enviar el log. Código de estado: {response.status_code}")
            print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")


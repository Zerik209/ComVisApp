# Programas utilizando Flask

:::info
:bulb: Programa cliente servidor utilizando Python, Flask y Azure, con arquitecturas SOAP y REST
:::

## Manual de Operacion
    
:::success
1. Clona el repositorio en cualquier carpeta
2. Crea un entorno virtual de python
3. Instalar todas las librerias necesarias
4. Corre XAMP con MySQL para tener lista la base de datos
5. Corre el servidro.py
6. Ejecuta el cliente.py
7. Abre el link generado en local host por el servidor
::: 
    
## Manual de desarrollo

1. Primero se crea un entorno virtual en python para instalar todas las librerias necesarias que haran funcionar los imports

```
import mysql.connector
from flask import Flask, request, jsonify, render_template
from io import BytesIO
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
```

2. Configura tu base de datos
```
# Configurar la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='dbanaimg'
)

# Obtener un cursor para ejecutar consultas SQL
cursor = db.cursor()
```
3. Configura tus credenciales de azure
```
# Configurar las credenciales de Azure
subscription_key = "0ejemplo02020"
endpoint = "https://ejemplo.cognitiveservices.azure.com/"

```
4. Implementa tu codigo para obtener la respuesta de azure y guardarlo en la base de datos

5. Configura tu cliente para subir las imagenes y ejecutar las consultas en el servidor

## Capturas

![Texto alternativo](/capturas/1.png)
![Texto alternativo](/capturas/2.png)
![Texto alternativo](/capturas/3.png)
![Texto alternativo](/capturas/4.png)


## Creditos
- Erik Aban
- Marisol Ac
- Daniel Panti
- Eduardo Corea

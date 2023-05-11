import mysql.connector
from flask import Flask, request, jsonify, render_template
from io import BytesIO
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

app = Flask(__name__)

# Configurar la conexión a la base de datos MySQL
db = mysql.connector.connect(
    host='localhost',
    user='tu_usuario',
    password='tu_contraseña',
    database='nombre_de_tu_basededatos'
)

# Obtener un cursor para ejecutar consultas SQL
cursor = db.cursor()

# Configurar las credenciales de Azure
subscription_key = "tu_clave_de_suscripción"
endpoint = "tu_endpoint"

# Configurar el cliente de Computer Vision
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(subscription_key))

# Crear tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS images (
        id INT AUTO_INCREMENT PRIMARY KEY,
        file_name VARCHAR(255) NOT NULL,
        description TEXT
    )
""")
db.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-image', methods=['POST'])
def upload_image():
    # Obtener la imagen del cuerpo de la solicitud y guardarla en la base de datos
    image_file = request.files['image']
    image_data = image_file.read()

    # Guardar la imagen en la base de datos
    query = "INSERT INTO images (file_name) VALUES (%s)"
    cursor.execute(query, (image_file.filename,))
    db.commit()

    # Obtener el ID de la imagen recién guardada
    image_id = cursor.lastrowid

    # Analizar la imagen con Computer Vision
    image_analysis = computervision_client.analyze_image_in_stream(BytesIO(image_data), ["description"])

    # Obtener la descripción de la imagen
    image_description = image_analysis.description.captions[0].text

    # Guardar la descripción en la base de datos
    query = "UPDATE images SET description = %s WHERE id = %s"
    cursor.execute(query, (image_description, image_id))
    db.commit()

    return jsonify({'description': image_description})

@app.route('/image-history', methods=['GET'])
def image_history():
    # Obtener el historial de imágenes de la base de datos
    query = "SELECT id, file_name, description FROM images"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Convertir los resultados en una lista de diccionarios
    image_history = []
    for row in rows:
        image = {
            'id': row[0],
            'file_name': row[1],
            'description': row[2]
        }
        image_history.append(image)

    return jsonify(image_history)

if __name__ == '__main__':
    app.run(debug=True, port=5000)



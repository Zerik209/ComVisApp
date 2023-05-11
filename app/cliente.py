import requests

def upload_image(file_path):
    url = "http://localhost:5000/upload-image"

    with open(file_path, 'rb') as file:
        files = {'image': file}
        response = requests.post(url, files=files)

    if response.status_code == 200:
        print("Imagen cargada con éxito")
    else:
        print("Error al cargar la imagen")

def get_image_history():
    url = "http://localhost:5000/image-history"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print("Historial de imágenes:")
        for item in data:
            print("Imagen: ", item['file_name'])
            print("Descripción: ", item['description'])
            print()
    else:
        print("Error al obtener el historial de imágenes")

if __name__ == '__main__':
    file_path = "ruta_de_tu_imagen.jpg"
    upload_image(file_path)

    get_image_history()

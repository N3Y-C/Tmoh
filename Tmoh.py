import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import os

while True:
    # Pedir al usuario que ingrese la URL del sitio web o escriba "exit" para salir
    url = input("Ingresa la URL del sitio web o escribe 'exit' para salir: ")

    # Si el usuario escribe "exit", salir del ciclo
    if url == "exit":
        break

    # Simular el comportamiento de un navegador web
    headers = {'User-Agent': UserAgent().chrome,
               'Referer': url
               }

    # Realizar la solicitud HTTP y obtener el contenido de la página
    response = requests.get(url, headers=headers)

    # Comprobar si se pudo obtener el código fuente
    if response.status_code == 200:
        # Crear el objeto BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Obtener el nombre de la página web
        page_name = soup.select_one('div.col-xs-12.text-center h1.reader-title').text.strip()

        # Nombre de la carpeta donde se guardarán las imágenes descargadas
        folder_name = page_name.replace(' ', '_') + '_img'

        # Comprobar si la carpeta existe, y si no, crearla
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)

        # Buscar todas las etiquetas img que tienen un atributo "data-original"
        img_tags = soup.find_all('img', {'data-original': True})

        # Descargar cada imagen en la carpeta correspondiente con el formato .jpg
        for img in img_tags:
            img_url = img['data-original']
            response = requests.get(img_url, headers=headers)
            filename = os.path.basename(img_url)
            img_local_path = os.path.join(folder_name, f'{os.path.splitext(filename)[0]}.jpg')
            with open(img_local_path, 'wb') as f:
                f.write(response.content)
            print(f'Imagen descargada: {os.path.basename(img_local_path)}')

            # Modificar el atributo src para que apunte al archivo jpg local
            img['src'] = os.path.basename(img_local_path)

        # Crear el archivo HTML con las imágenes descargadas
        html = BeautifulSoup("<html><head><style>img {display: block; margin: 0 auto;} body {text-align: center; background-color: black;}</style></head><body></body></html>", 'html.parser')
        for img in img_tags:
            html.body.append(img)
            html.body.append(html.new_tag('br'))

        # Guardar el archivo HTML en la carpeta correspondiente
        with open(os.path.join(folder_name, f'{page_name}.html'), 'w') as f:
            f.write(str(html))
            print(f'Archivo HTML guardado: {page_name}.html')
    else:
        print('Error al obtener el código fuente:', response.status_code)

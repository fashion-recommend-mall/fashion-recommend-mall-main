import asyncio
import os
from datetime import datetime

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import requests

deep_learning_server_url = "http://localhost:3000"
img_path = 'http://host.docker.internal:8000/'

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

def get_style_service(files : dict):

    file_path = 'static/media' + f'/{datetime.now().strftime("%Y-%m-%d-%H-%M-%S")}'

    os.makedirs(file_path)

    return get_style_from_deep_learning_server(files, file_path)


def get_style_from_deep_learning_server(files, file_path):

    style_dict = {
        "traditional" : 0,
        "manish" : 0,
        "feminine" : 0,
        "ethnic" : 0,
        "contemporary" : 0,
        "natural" : 0,
        "genderless" : 0,
        "sporty" : 0,
        "subculture" : 0,
        "casual" : 0
    }

    for index, file in enumerate(files):

        path = default_storage.save( file_path + f'/{index}.jpeg', ContentFile(files[file].read()))

        style = requests.get(f'{deep_learning_server_url}/upload?img_path={img_path+path}').json()

        style_dict[style["first style"]] += 2
        style_dict[style["second style"]] += 1
    
    for style in style_dict:
        target = style_dict[style]
        if target != 0:
            style_dict[style] = int(style_dict[style] / 30 * 100 + 0.5)

    return style_dict
        
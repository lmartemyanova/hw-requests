from pprint import pprint

import requests

class YandexDisk:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        headers = {
            'Accept': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        return headers

    def get_upload_link(self, file_path):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path}
        response = requests.get(url, headers=headers, params=params).json()
        href = response['href']
        return href

    def upload(self, file_path):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        href = self.get_upload_link(file_path)
        response = requests.put(href)
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
            return
        else:
            print("Try again")
            return

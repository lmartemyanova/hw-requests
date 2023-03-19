import requests
import os

from ya_disk_token import TOKEN
from ya_disk import YandexDisk


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    input_path = input('Введите путь к загружаемому файлу на компьютере: ')
    # disk_path = input('Введите путь к папке на диске (нажмите enter, если файл нужно загрузить в "Файлы": ')
    file_path = os.path.basename(input_path)
    token = TOKEN
    uploader = YandexDisk(token)
    result = uploader.upload(file_path)
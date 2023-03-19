import requests
import os

from superheroes import Superheroes, compare_intelligence
from ya_disk import YandexDisk


if __name__ == '__main__':
    hulk = Superheroes('Hulk')
    cap = Superheroes('Captain America')
    thanos = Superheroes('Thanos')

    print(compare_intelligence(hulk, cap, thanos))


    input_path = input("Введите путь к загружаемому файлу на компьютере: ")
    file_path = os.path.basename(input_path)
    token = input("Введите токен: ")

    uploader = YandexDisk(token)
    result = uploader.upload(input_path, file_path)

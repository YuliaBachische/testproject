import csv
from typing import List, Dict, Optional
import logging

logging.basicConfig(level=logging.DEBUG)
USERS_CSV = 'C:/Users/USER/PycharmProjects/pythonProject3/app/data/users.csv'
NOTES_CSV = 'C:/Users/USER/PycharmProjects/pythonProject3/app/data/notes.csv'


def read_csv(file_path: str) -> List[Dict[str, str]]:
    """
    Читает данные из CSV-файла и возвращает их в виде списка словарей.

    :param file_path: Путь к CSV-файлу для чтения.
    :return: Список словарей, где каждый словарь представляет собой строку из CSV-файла.
    :raises FileNotFoundError: Если файл не найден по указанному пути.
    :raises IOError: Если возникает ошибка ввода/вывода при работе с файлом.
    """
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)


def write_csv(file_path: str, data: List[Dict[str, str]]) -> None:
    """
    Записывает данные в CSV-файл. Если данных нет, файл не будет записан.

    :param file_path: Путь к CSV-файлу для записи.
    :param data: Список словарей, содержащих данные для записи в CSV-файл.
    :return: None
    :raises IOError: Если возникает ошибка ввода/вывода при работе с файлом.
    """
    if not data:
        return

    fieldnames = data[0].keys()

    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


def get_user(username: str) -> Optional[Dict[str, str]]:
    """
    Получает информацию о пользователе по имени пользователя из CSV-файла.

    :param username: Имя пользователя для поиска.
    :return: Словарь с данными пользователя, если пользователь найден, иначе None.
    :raises FileNotFoundError: Если файл пользователей не найден.
    :raises IOError: Если возникает ошибка ввода/вывода при работе с файлом.
    """
    users = read_csv(USERS_CSV)
    for user in users:
        if user['username'] == username:
            return user
    return None

import csv
import logging
from app.crud import write_csv, read_csv

logging.basicConfig(level=logging.DEBUG)

NOTES_CSV = 'app/data/notes.csv'


def read_notes_from_csv() -> list[str]:
    """
    Читает заметки из CSV-файла и возвращает их в виде списка словарей.

    :return: Список словарей, где каждый словарь представляет собой строку из CSV-файла с заметками.
    :raises FileNotFoundError: Если файл заметок не найден по указанному пути.
    :raises Exception: Для обработки других неожиданных ошибок.
    """
    notes = []
    try:
        with open(NOTES_CSV, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                notes.append(row)
    except FileNotFoundError:
        print("File not found, make sure DATA_FILE is correct")
    except Exception as e:
        print(f"An error occurred: {e}")
    logging.debug(f"Notes read: {notes}")
    return notes


def add_note(user_id: str, title: str, content: str) -> None:
    """
    Добавляет новую заметку в CSV-файл.

    :param user_id: Идентификатор пользователя, которому принадлежит заметка.
    :param title: Заголовок заметки.
    :param content: Содержание заметки.
    :return: None
    :raises Exception: Для обработки неожиданных ошибок, таких как ошибка записи в файл.
    """
    notes = read_csv(NOTES_CSV)
    new_id = str(len(notes) + 1)
    new_note = {
        'id': new_id,
        'user_id': user_id,
        'title': title,
        'content': content
    }
    logging.debug(f"Adding note: {new_note}")

    notes.append(new_note)
    write_csv(NOTES_CSV, notes)



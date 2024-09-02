import pytest
import tempfile
import shutil
from app.crud import write_csv, read_csv
from app.utils import add_note


@pytest.fixture
def temp_notes_csv():
    """
    Фикстура для создания временного CSV-файла. Этот файл используется для тестов, чтобы
    избежать изменений в реальных данных. После завершения тестов временный файл и
    директория удаляются.

    :yield: Путь к временному CSV-файлу.
    """
    temp_dir = tempfile.mkdtemp()
    temp_file = tempfile.NamedTemporaryFile(delete=False, dir=temp_dir, suffix='.csv')
    temp_file.close()
    yield temp_file.name
    shutil.rmtree(temp_dir)


def test_add_note(temp_notes_csv):
    """
    Проверяет функцию `add_note` для добавления новой заметки в CSV-файл.

    1. Создаем начальные данные и записываем их в временный CSV-файл.
    2. Добавляем новую заметку с помощью функции `add_note`.
    3. Читаем обновленный CSV-файл и проверяем, что заметка была добавлена.

    :param temp_notes_csv: Путь к временному CSV-файлу, предоставленный фикстурой.
    """
    initial_data = [
        {'id': '1', 'user_id': '1', 'title': 'Note 1', 'content': 'Content 1'},
        {'id': '2', 'user_id': '1', 'title': 'Note 2', 'content': 'Content 2'}
    ]
    write_csv(temp_notes_csv, initial_data)

    global NOTES_CSV
    NOTES_CSV = temp_notes_csv

    add_note('1', 'New Note', 'This is a new note')

    notes = read_csv(temp_notes_csv)
    assert len(notes) == 2



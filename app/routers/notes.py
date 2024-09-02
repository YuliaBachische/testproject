from fastapi import APIRouter, Depends, HTTPException
from typing import Dict, Optional, Union, List

from ..auth import get_current_user
from ..models import NoteCreate
from ..spell_check import check_spelling_in_text
from ..utils import read_notes_from_csv, add_note

router = APIRouter(
    prefix="/notes",
    tags=["notes"],
    responses={404: {"description": "Not found"}},
)


@router.post("/")
async def create_note(
        note: NoteCreate,
        current_user: Dict = Depends(get_current_user)
) -> Optional[dict[str, Union[str, list[dict]]]]:
    """
    Создает новую заметку с исправлением орфографических ошибок в заголовке и содержании.

    - **note**: Объект `NoteCreate` с полями `title` и `content`, представляющими заголовок и содержание заметки.
    - **current_user**: Текущий пользователь, полученный через зависимость `get_current_user`.

    Возвращает объект с полем `message` и, при наличии орфографических ошибок, полем `errors`:
    - **message**: Сообщение о результате добавления заметки.
    - **errors**: Список исправленных орфографических ошибок (если таковые имеются).

    Если данные о заметке содержат орфографические ошибки, они будут возвращены в поле `errors`.
    """
    title = note.title
    content = note.content

    corrected_title, corrected_content, spelling_errors = check_spelling_in_text(title, content)

    add_note(current_user["username"], corrected_title, corrected_content)

    if spelling_errors:
        return {"message": "Note added with spelling corrections", "errors": spelling_errors}

    return {"message": "Note added successfully"}


@router.get("/")
async def list_notes(current_user: Dict = Depends(get_current_user)) -> List[Dict[str, str]]:
    """
    Получает список заметок для текущего пользователя.

    - **current_user**: Текущий пользователь, полученный через зависимость `get_current_user`.

    Возвращает список заметок пользователя:
    - Каждая заметка содержит поля `id`, `title`, `content`, и `user_id`.
    """
    notes = read_notes_from_csv()
    user_notes = [note for note in notes if note["user_id"] == current_user["username"]]
    return user_notes

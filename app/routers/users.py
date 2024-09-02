from typing import Dict

from fastapi import APIRouter, Query
from ..auth import get_current_user

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


@router.get("/me")
async def get_user_info(username: str = Query(...), password: str = Query(...)) -> Dict:
    """
    Получает информацию о текущем пользователе на основе предоставленных имени пользователя и пароля.

    - **username**: Имя пользователя для аутентификации.
    - **password**: Пароль пользователя для аутентификации.

    Возвращает словарь с именем пользователя:
    - **username**: Имя пользователя.
    """
    user = get_current_user(username=username, password=password)
    return {"username": user["username"]}

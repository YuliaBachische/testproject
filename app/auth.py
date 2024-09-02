from typing import Optional
from fastapi import HTTPException, status, Query

from app.crud import get_user


def verify_password(plain_password: str, stored_password: str) -> bool:
    """
     Проверяет совпадение между введенным паролем и хранящимся паролем.

     В данной реализации пароли сравниваются напрямую без использования хеширования.

     :param plain_password: Введенный пользователем пароль.
     :param stored_password: Хранящийся пароль (обычно хешированный).
     :return: True, если пароли совпадают, иначе False.
     """
    return plain_password == stored_password


def authenticate_user(username: str, password: str) -> Optional[dict]:
    """
    Аутентифицирует пользователя по имени и паролю.

    Выполняет следующие действия:
    1. Получает данные пользователя по имени.
    2. Сравнивает введенный пароль с хранящимся паролем.

    :param username: Имя пользователя для аутентификации.
    :param password: Пароль пользователя для проверки.
    :return: Данные пользователя в виде словаря, если аутентификация успешна, иначе None.
    """
    user = get_user(username)
    if not user or not verify_password(password, user['password']):
        return None
    return user


def get_current_user(username: str = Query(...), password: str = Query(...)) -> dict:
    """
    Извлекает текущего пользователя на основе имени и пароля, переданных в запросе.

    Если аутентификация неудачна, вызывает исключение HTTP 401.

    :param username: Имя пользователя из запроса.
    :param password: Пароль пользователя из запроса.
    :return: Данные текущего пользователя в виде словаря.
    :raises HTTPException: Если аутентификация не удалась, вызывается исключение HTTP 401.
    """
    user = authenticate_user(username, password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication credentials")
    return user

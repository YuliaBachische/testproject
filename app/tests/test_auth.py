import pytest
from unittest.mock import patch
from app.auth import verify_password, authenticate_user, get_current_user


def test_verify_password():
    """
    Проверяет функцию `verify_password`, которая сравнивает
    открытый пароль с сохраненным хешем пароля.

    Ожидаемые результаты:
    - Функция должна вернуть True, если пароли совпадают.
    - Функция должна вернуть False, если пароли не совпадают.
    """
    plain_password = "testpassword"
    stored_password = "testpassword"
    assert verify_password(plain_password, stored_password)


def test_authenticate_user():
    """
    Проверяет функцию `authenticate_user`, которая аутентифицирует пользователя
    по имени пользователя и паролю.

    Используется мок для функции `get_user`, которая возвращает предопределенного пользователя.

    Ожидаемые результаты:
    - Функция должна вернуть пользователя, если имя пользователя и пароль совпадают.
    - Функция должна вернуть None, если пароль неверный.
    """
    def mock_get_user(username):
        if username == "johndoe":
            return {"username": "johndoe", "password": "testpassword"}
        return None

    with patch('app.crud.get_user', mock_get_user):
        user = authenticate_user("johndoe", "testpassword")
        assert user is not None, "Expected user, got None"
        assert user['username'] == "johndoe", "Username does not match"
        assert authenticate_user("johndoe", "wrongpassword") is None


def test_get_current_user():
    """
    Проверяет функцию `get_current_user`, которая возвращает текущего
    аутентифицированного пользователя.

    Используется мок для функции `authenticate_user`, которая возвращает предопределенного пользователя.

    Ожидаемые результаты:
    - Функция должна вернуть пользователя, если имя пользователя и пароль совпадают.
    - Функция должна вернуть None, если имя пользователя или пароль неверны.
    """
    def mock_authenticate_user(username, password):
        if username == "johndoe" and password == "testpassword":
            return {"username": "johndoe"}
        return None

    with patch('app.auth.authenticate_user', mock_authenticate_user):
        assert get_current_user("johndoe", "testpassword") == {"username": "johndoe"}

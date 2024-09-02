from pydantic import BaseSettings


class Settings(BaseSettings):
    # Основные параметры приложения
    APP_NAME: str = "My FastAPI Application"
    DEBUG: bool = False

    # Параметры безопасности
    SECRET_KEY: str = "supersecretkey"  # Это значение лучше хранить в переменных окружения
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Настройки базы данных
    DATABASE_URL: str = "sqlite:///./test.db"  # Пример для SQLite, но можно использовать PostgreSQL, MongoDB и т.д.

    # Настройки для интеграции с внешними сервисами
    SPELL_CHECK_SERVICE_URL: str = "http://spellcheck-service/api/check"
    SPELL_CHECK_API_KEY: str = "apikey"

    class Config:
        env_file = ".env"  # Путь к файлу с переменными окружения


# Создаем экземпляр настроек, который будет использоваться в приложении
settings = Settings()
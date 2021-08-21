import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    PROJECT_TITLE: str = os.getenv("PROJECT_TITLE")
    PROJECT_VERSION: str = "0.2.7"
    POSTGRES_USER: str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER: str = os.getenv("POSTGRES_SERVER")
    POSTGRES_PORT: str = os.getenv("POSTGRES_PORT")
    POSTGRES_DB: str = os.getenv("POSTGRES_DB")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"

    ACCESS_TOKEN_EXPIRES_MINUTES: int = os.getenv("ACCESS_TOKEN_EXPIRES_MINUTES")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM")

    TEST_USER_EMAIL: str = os.getenv("TEST_USER_EMAIL")


settings = Settings()

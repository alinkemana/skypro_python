import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    BASE_URL: str = os.getenv("BASE_URL", "https://api.kinopoisk.dev")
    API_TOKEN: str = os.getenv("API_TOKEN")


settings = Settings()

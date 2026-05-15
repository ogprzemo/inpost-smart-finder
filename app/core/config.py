from pydantic import BaseSettings


class Settings(BaseSettings):
    INPOST_API_URL: str = "https://api-global-points.easypack24.net/v1/points"
    PAGE_SIZE: int = 100

    class Config:
        env_file = ".env"


settings = Settings()
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import computed_field


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    BIBLE_VERSION: str = "lsg"
    REFRESH_INTERVAL: int = 30

    @computed_field
    def REFRESH_INTERVAL_MS(self) -> int:
        return self.REFRESH_INTERVAL * 1000


settings = Settings()

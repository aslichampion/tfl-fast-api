from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")

    TRACKERNET_API_KEY: str


settings = Settings()  # type: ignore

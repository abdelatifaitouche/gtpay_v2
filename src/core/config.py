from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "GTPAY"

    DATABASE_URL: str

    DEBUG: bool

    # jwt configs
    JWT_SECRET_KEY: str
    JWT_ALGO: str
    ACCESS_TOKEN_TIME: int
    REFRESH_TOKEN_TIME: int

    MINIO_ENDPOINT: str
    MINIO_ACCESS_KEY: str
    MINIO_SECRET_KEY: str
    MINIO_IS_SECURE: bool
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()

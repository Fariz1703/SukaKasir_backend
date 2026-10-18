from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str


    FILEBASE_ACCESS_KEY: str
    FILEBASE_SECRET_KEY: str
    FILEBASE_BUCKET: str
    
    class Config:
        env_file = ".env"


settings = Settings()
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str
    SECRET_KEY: str
    
    DATABASE_NAME: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_USER: str
    DATABASE_PASSWORD: str

    class Config:
        env_file = ".env"

    @property
    def database_url(self):
        return (
            f"postgresql://{self.DATABASE_USER}:{self.DATABASE_PASSWORD}"
            f"@{self.DATABASE_HOST}:{self.DATABASE_PORT}/{self.DATABASE_NAME}"
        )

settings = Settings()
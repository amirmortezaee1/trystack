from pydantic import BaseSettings

class Settings(BaseSettings):
     enviroment="development"

settings = Settings()
from pydantic import BaseSettings, SecretStr


class Settings(BaseSettings):
    token: SecretStr
    payments_token: SecretStr
    admin_id: SecretStr

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


config = Settings()

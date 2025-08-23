from pydantic import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = 'flight-delay'
    APP_VERSION: str = '1.0.0'
    BASE_PATH: str = f'/api/{APP_NAME}'

    MODELS_BUCKET_NAME: str = ''
    DELAY_THRESHOLD: int = 15
    project_id: str = ''
    dataset_id: str = ''
    table_id: str = ''

    REDIS_HOST: str = ""
    REDIS_PORT: int = 6379

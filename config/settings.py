from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MODEL_NAME: str = "qwen3.5:4b"
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"
    CHROMA_PATH: str = "chroma_db"
    TOP_K: int = 4

settings = Settings()
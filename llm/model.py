from langchain_ollama import ChatOllama
from config.settings import settings

def get_llm():

    return ChatOllama(
        model = settings.MODEL_NAME,
        temperature= 0.2
    )
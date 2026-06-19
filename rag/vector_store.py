from langchain_chroma import Chroma
from rag.embeddings import get_embeddings
from config.settings import settings

def vector_store():

    return Chroma(
        persist_directory=settings.CHROMA_PATH,
        embedding_function=get_embeddings()
    )
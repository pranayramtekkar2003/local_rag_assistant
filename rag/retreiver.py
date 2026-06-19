from rag.vector_store import vector_store
from config.settings import settings

def retriever():
    
    vectorDB = vector_store()

    return vectorDB.as_retriever(
        search_kwargs={
            "k": settings.TOP_K
        }
    )
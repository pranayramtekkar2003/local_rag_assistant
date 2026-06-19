import os
from langchain_community.document_loaders import PyPDFLoader

def load_documents(directory):
    docs = []

    for file in os.listdir(directory):

        if file.endswith(".pdf"):

            path = os.path.join(
                directory,
                file
            )

            pdf_doc = PyPDFLoader(path).load()

            for doc in pdf_doc:
                doc.metadata["source"] = file
            
            docs.extend(pdf_doc)
        
        return docs
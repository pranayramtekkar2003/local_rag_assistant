from rag.retreiver import get_retriever

from llm.structured_output import get_strutured_llm

def retrieverNode(state):
    retriever = get_retriever()

    docs = retriever.invoke(
        state["question"]
    )

    context = '\n'.join(
        doc.page_content
        for doc in docs
    )

    metadata = {
        "sources" : [
            doc.metadata
            for doc in docs
        ]
    }

    return {
        "context": context,
        "metadata": metadata
    }

def generateNode(state):
    llm = get_strutured_llm()

    prompt = f"""
Context: {state["context"]}
Question: {state["question"]}
"""
    result = llm.invoke(prompt)

    return {
        "answer": result.answer
    }
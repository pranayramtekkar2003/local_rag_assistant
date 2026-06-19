from llm.model import get_llm
from schema.response_schema import AssistantResponse

def get_strutured_llm():
    llm = get_llm()

    return llm.with_structured_output(
        AssistantResponse
    )

## Multi -PDF ingestion
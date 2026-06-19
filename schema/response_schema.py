from pydantic import BaseModel, Field

class AssistantResponse(BaseModel):
    ans: str = Field(description="Answer for the user")
    source: str = Field(description="Source of the answer")
    confidence: float = Field(description="Confidence score for the answer")
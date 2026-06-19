from pydantic import BaseModel, Field

class Query(BaseModel):
    question: str = Field(description="Query provided by the user")

class Response(BaseModel):
    ans: str
    latency: float
    token_generated: int
    token_per_sec: float
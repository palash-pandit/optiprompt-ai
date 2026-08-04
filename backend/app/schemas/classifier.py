from pydantic import BaseModel


class ClassifierRequest(BaseModel):
    text: str


class ClassifierResponse(BaseModel):
    prompt_type: str
    confidence: float
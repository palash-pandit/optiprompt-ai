from pydantic import BaseModel


class QualityRequest(BaseModel):
    text: str


class QualityResponse(BaseModel):
    score: int
    grade: str
    metrics: dict
    suggestions: list[str]
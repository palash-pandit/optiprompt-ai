from pydantic import BaseModel


class StrategyRequest(BaseModel):
    prompt_type: str
    quality_score: int
    user_mode: str = "Balanced"


class StrategyResponse(BaseModel):
    strategy: str
    reason: list[str]
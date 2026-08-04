from pydantic import BaseModel


class APOERequest(BaseModel):
    text: str
    user_mode: str = "Balanced"


class APOEResponse(BaseModel):
    original_prompt: str
    optimized_prompt: str
    optimization_applied: bool

    quality_score: int
    prompt_type: str
    strategy: str

    reasons: list[str]

    tokens_before: int
    tokens_after: int
    tokens_saved: int
    reduction_percentage: float

    estimated_cost_before: float
    estimated_cost_after: float
    estimated_savings: float
from fastapi import APIRouter

from app.schemas.strategy import StrategyRequest
from app.services.strategy_selector_service import (
    StrategySelectorService,
)

router = APIRouter(
    prefix="/strategy",
    tags=["Strategy Selector"],
)

service = StrategySelectorService()


@router.post("/select")
def select_strategy(request: StrategyRequest):

    return service.select_strategy(
        request.prompt_type,
        request.quality_score,
        request.user_mode,
    )
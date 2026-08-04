from fastapi import APIRouter

from app.schemas.apoe import APOERequest
from app.services.apoe_engine import APOEEngine

router = APIRouter(
    prefix="/apoe",
    tags=["APOE Engine"]
)

engine = APOEEngine()


@router.post("/optimize")
def optimize(request: APOERequest):

    return engine.optimize(
        request.text,
        request.user_mode
    )
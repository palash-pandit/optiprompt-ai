from fastapi import APIRouter

from app.services.pricing_manager import PricingManager

router = APIRouter(
    prefix="/pricing",
    tags=["Pricing"]
)

manager = PricingManager()


@router.get("/models")
def get_models():

    return manager.get_all_models()
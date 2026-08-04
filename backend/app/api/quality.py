from fastapi import APIRouter

from app.schemas.quality import QualityRequest
from app.services.prompt_quality_service import PromptQualityService

router = APIRouter(
    prefix="/quality",
    tags=["Prompt Quality"]
)

service = PromptQualityService()


@router.post("/analyze")
def analyze(request: QualityRequest):
    return service.analyze(request.text)
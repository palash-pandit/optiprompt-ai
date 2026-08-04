from fastapi import APIRouter

from app.schemas.classifier import ClassifierRequest
from app.services.prompt_classifier_service import PromptClassifierService

router = APIRouter(
    prefix="/classifier",
    tags=["Prompt Classifier"]
)

service = PromptClassifierService()


@router.post("/classify")
def classify(request: ClassifierRequest):
    return service.classify(request.text)
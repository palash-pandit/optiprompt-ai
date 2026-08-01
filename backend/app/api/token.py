from fastapi import APIRouter

from app.schemas.token import TokenRequest
from app.services.token_service import TokenService

router = APIRouter()

service=TokenService()

@router.post("/analyze")
def analyze(request: TokenRequest):
    return service.analyze(request.text)
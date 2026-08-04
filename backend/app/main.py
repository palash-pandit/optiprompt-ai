from fastapi import FastAPI
from app.api.token import router as token_router
from app.api.pricing import router as pricing_router
from app.api.quality import router as quality_router
from app.api.classifier import router as classifier_router


app=FastAPI(title="OptiPrompt AI",
            description="LLM Token Optimization Platform",
            version="0.1.0")

app.include_router(token_router)
app.include_router(pricing_router)
app.include_router(quality_router)
app.include_router(classifier_router)

@app.get("/")
def root():
    return{
        "message":"Welcome to OptiPrompt AI",
        
    }
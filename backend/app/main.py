from fastapi import FastAPI
from app.api.token import router as token_router

app=FastAPI(title="OptiPrompt AI",
            description="LLM Token Optimization Platform",
            version="0.1.0")

app.include_router(token_router)

@app.get("/")
def root():
    return{
        "message":"Welcome to OptiPrompt AI",
        
    }